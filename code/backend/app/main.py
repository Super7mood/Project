from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import bcrypt
import os
import sys
import datetime
from dotenv import load_dotenv
from typing import Optional

# Add 'backend/llm' folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'llm')))

# Import LLM models
from llm.chatGPT import chatGPT
from llm.gemini import gemini
from llm.claude import claude
from llm.call import callChatBots

# Firestore Setup
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize FastAPI
app = FastAPI()

# Enable CORS for all routes or specify the frontend domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load environment from .env
load_dotenv()

# Firebase JSON key
cred = credentials.Certificate("../firebase-adminsdk.json")  # Ensure this matches your file name
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

# Pydantic models for request validation
class UserRegistration(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class QuestionRequest(BaseModel):
    question: str
    email: Optional[str] = "default@example.com"

class QueryRequest(BaseModel):
    query: str

class TestDataRequest(BaseModel):
    email: str
    question: str
    response: str

# Root endpoint
@app.get("/")
def home():
    return {"message": "Welcome to AI Checker Pro API", "description": "Use the API endpoints to interact with the system."}

# Register endpoint
@app.post("/register")
def register_user(user: UserRegistration):
    email = user.email
    password = user.password

    if not email or not password:
        raise HTTPException(status_code=400, detail="Email and password are required")

    # Check if user already exists
    users_ref = db.collection("users").where("email", "==", email).stream()
    if any(users_ref):
        raise HTTPException(status_code=400, detail="User already exists!")

    # Hash the password before storing it
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Store user in Firestore
    db.collection("users").add({
        "email": email,
        "password": hashed_password.decode('utf-8'),  # Store as string
        "created_at": datetime.datetime.now(datetime.timezone.utc)
    })
    return {"message": "User registered successfully!"}

# Login endpoint
@app.post("/login")
def login_user(user: UserLogin):
    email = user.email
    password = user.password

    users_ref = db.collection("users").where("email", "==", email).stream()
    user_data = None
    for user in users_ref:
        user_data = user.to_dict()

    if not user_data:
        raise HTTPException(status_code=404, detail="User not found!")

    # Verify hashed password
    if bcrypt.checkpw(password.encode('utf-8'), user_data["password"].encode('utf-8')):
        return {"message": "Login successful!"}
    else:
        raise HTTPException(status_code=400, detail="Incorrect password!")

# Ask endpoint
@app.post("/ask")
def ask_question(question_request: QuestionRequest):
    question = question_request.question
    email = question_request.email

    if not question:
        raise HTTPException(status_code=400, detail="No question provided")

    # Call LLM models
    llmResponses = callChatBots(question)

    # Get responses from each LLM model
    chatgpt_response = llmResponses["ChatGPT"][0]
    gemini_response = llmResponses["Gemini"][0]
    claude_response = llmResponses["Claude"][0]

    # Ensure responses are valid strings
    chatgpt_response = chatgpt_response if isinstance(chatgpt_response, str) else str(chatgpt_response)
    gemini_response = gemini_response if isinstance(gemini_response, str) else str(gemini_response)
    claude_response = claude_response if isinstance(claude_response, str) else str(claude_response)

    # Scoring the responses
    scores = {
        "chatgpt": score_response(chatgpt_response),
        "gemini": score_response(gemini_response),
        "claude": score_response(claude_response) if not claude_response.startswith("Claude API") else 0
    }

    # Store responses in dictionary
    responses = {
        "chatgpt": {"response": chatgpt_response, "score": scores["chatgpt"]},
        "gemini": {"response": gemini_response, "score": scores["gemini"]},
        "claude": {"response": claude_response, "score": scores["claude"]}
    }

    # Sort responses based on scores (highest first)
    ranked_responses = dict(sorted(responses.items(), key=lambda item: item[1]["score"], reverse=True))

    # Store in Firestore
    db.collection("submissions").add({
        "user_email": email,
        "question": question,
        "responses": responses,
        "timestamp": datetime.datetime.now(datetime.timezone.utc)
    })

    return ranked_responses

# Query endpoint
@app.post("/api/query")
def query(query_request: QueryRequest):
    query_text = query_request.query
    response = chatGPT(query_text)
    return {"response": response}

# Add test data endpoint
@app.post("/add_test_data")
def add_test_data(test_data: TestDataRequest):
    db.collection("submissions").add({
        "email": test_data.email,
        "question": test_data.question,
        "response": test_data.response,
        "timestamp": datetime.datetime.now(datetime.timezone.utc)
    })
    return {"message": "Test data added successfully!"}

# Helper function to score responses
def score_response(response):
    return len(response)  # Simple example: longer responses score higher

# Run the application
if __name__ == "__main__":
    import uvicorn
    # Run uvicorn main:app --host 127.0.0.1 --port 5000
    uvicorn.run(app, host="127.0.0.1", port=5000)