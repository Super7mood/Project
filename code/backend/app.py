from flask import Flask, request, jsonify
import bcrypt
import os
import sys
import datetime
from dotenv import load_dotenv

# Add 'backend/llm' folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'llm')))

# Import LLM models
from llm.call import callChatBots

from flask_cors import CORS

# Firestore Setup
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Flask
app = Flask(__name__)

# Enable CORS for all routes or specify the frontend domain
CORS(app, origins="http://localhost:3000")  # Ensure only frontend domain can access

# Load environment from .env
load_dotenv()

# Firebase JSON key
cred = credentials.Certificate("firebase-adminsdk.json")  # Ensure this matches your file name
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

@app.route("/")
def home():
    return "<h1>Welcome to AI Checker Pro API</h1><p>Use the API endpoints to interact with the system.</p>"

@app.route("/register", methods=["POST"])
def register_user():
    data = request.json
    email = data.get("email")
    password = data.get("password")
    
    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400

    # Check if user already exists
    users_ref = db.collection("users").where("email", "==", email).stream()
    if any(users_ref):
        return jsonify({"message": "User already exists!"}), 400

    # Hash the password before storing it
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Store user in Firestore
    db.collection("users").add({
        "email": email,
        "password": hashed_password.decode('utf-8'),  # Store as string
        "created_at": datetime.datetime.now(datetime.timezone.utc)
    })
    return jsonify({"message": "User registered successfully!"}), 200

@app.route("/login", methods=["POST"])
def login_user():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    users_ref = db.collection("users").where("email", "==", email).stream()
    user_data = None
    for user in users_ref:
        user_data = user.to_dict()

    if not user_data:
        return jsonify({"message": "User not found!"}), 404

    # Verify hashed password
    if bcrypt.checkpw(password.encode('utf-8'), user_data["password"].encode('utf-8')):
        return jsonify({"message": "Login successful!"}), 200
    else:
        return jsonify({"message": "Incorrect password!"}), 400

@app.route("/ask", methods=["POST"])
def ask_question():
    data = request.json
    question = data.get("question")
    email = data.get("email", "default@example.com")  # Ensure email is provided if required

    if not question:
        return jsonify({"error": "No question provided"}), 400
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

    # Debugging Log to Verify Response Before Returning
    print("🔍 AI Responses BEFORE Returning:", ranked_responses)

    return jsonify(ranked_responses), 200

@app.route("/api/query", methods=["POST"])
def query():
    data = request.json
    query_text = data.get("query", "")
    response = chatGPT(query_text)
    return jsonify({"response": response}), 200

@app.route("/add_test_data", methods=["POST"])
def add_test_data():
    test_data = {
        "email": "testuser@example.com",
        "question": "What is the capital of France?",
        "response": "Paris",
        "timestamp": datetime.datetime.now(datetime.timezone.utc)
    }
    db.collection("submissions").add(test_data)
    return jsonify({"message": "Test data added successfully!"}), 200

def score_response(response):
    return len(response)  # Simple example: longer responses score higher

if __name__ == "__main__":
    app.run(debug=True)
