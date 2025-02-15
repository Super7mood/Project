<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
import os, sys, path, requests
=======
import os, sys, requests
>>>>>>> 8d58dc2d74e74ec072fa5c5dd97a3ea680d3931c
from dotenv import load_dotenv
=======
>>>>>>> d897b26 (Revert "Moved call.py to app/servies folder for organisation")
from fastapi import APIRouter

<<<<<<< HEAD
=======
import os, sys, path, requests
=======
import os, sys, requests
>>>>>>> abba2f1 (Removed unused library)
from dotenv import load_dotenv
from fastapi import APIRouter

>>>>>>> 9bf6d44 (returned deleted file to resolve rebase issue)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from llm.call import callChatBots
from models.requestModels import LLMRequest
load_dotenv()
<<<<<<< HEAD
=======

>>>>>>> d897b26 (Revert "Moved call.py to app/servies folder for organisation")
router = APIRouter()


=======
router = APIRouter()

#Load API keys from enironment variables
chatGPTAPIKey = os.getenv("CHATGPT_API_KEY")
geminiAPIKey = os.getenv("GEMENI_API_KEY")
claudeAPIKey = os.getenv("CLAUDE_API_KEY")
>>>>>>> 9bf6d44 (returned deleted file to resolve rebase issue)



# class LLMRequests(BaseModel):
#     queries: List[LLMRequest]


# def fetch_response(api_url, api_key, prompt):
#     """Helper function to send API request to an LLM"""
#     try:
#         headers = {
#             "Authorization": f"Bearer {api_key}"
#         }

#         response = requests.post(api_url, json={"prompt": prompt}, headers=headers)
#         response.raise_for_status()
#         return response.json()
#     except requests.exceptions.RequestException as e:
#         return {"error": str(e)}

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
@router.post("/query")
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 234e38c (Revert "Revert "Moved call.py to app/servies folder for organisation"")
=======
@router.post("/prompt")
>>>>>>> abc2bdf (Removed some unused libraries and comments)
def query_llm(request: LLMRequest):
    """Handles incoming queries and sends them to multiple LLMs"""
<<<<<<< HEAD
    responses = {
        "Chatgpt": fetch_response("https://api.openai.com/v1/completions", chatGPTAPIKey, request.query),
        "Gemini": fetch_response("https://api.gemini.com/v1/completions", geminiAPIKey, request.query),
        "Claude": fetch_response("https://api.anthropic.com/v1/completions", claudeAPIKey, request.query),
    }
<<<<<<< HEAD
    return {"responses": responses}
=======
=======
=======
import os 
import requests
=======
import os, sys, path, requests
>>>>>>> ce9b745 (renamed services to llm and included all llm files in it)
from dotenv import load_dotenv
>>>>>>> 513022d (Moved call.py to app/servies folder for organisation)
=======
>>>>>>> 6e073d1 (Revert "Moved call.py to app/servies folder for organisation")
=======
import os 
import requests
from dotenv import load_dotenv
>>>>>>> 53f5c11 (Revert "Revert "Moved call.py to app/servies folder for organisation"")
=======
>>>>>>> 46ffaba (file to handle LLM API requests)
=======
import os 
import requests
from dotenv import load_dotenv
>>>>>>> e2bd6de (Moved call.py to app/servies folder for organisation)
=======
import os 
import requests
from dotenv import load_dotenv
>>>>>>> 234e38c (Revert "Revert "Moved call.py to app/servies folder for organisation"")
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from llm.call import callChatBots

>>>>>>> ce9b745 (renamed services to llm and included all llm files in it)
load_dotenv()
router = APIRouter()

#Load API keys from enironment variables
chatGPTAPIKey = os.getenv("CHATGPT_API_KEY")
geminiAPIKey = os.getenv("GEMENI_API_KEY")
claudeAPIKey = os.getenv("CLAUDE_API_KEY")
=======

router = APIRouter()


>>>>>>> 46ffaba (file to handle LLM API requests)
=======
load_dotenv()
router = APIRouter()

=======
load_dotenv()
router = APIRouter()

>>>>>>> 234e38c (Revert "Revert "Moved call.py to app/servies folder for organisation"")
#Load API keys from enironment variables
chatGPTAPIKey = os.getenv("CHATGPT_API_KEY")
geminiAPIKey = os.getenv("GEMENI_API_KEY")
claudeAPIKey = os.getenv("CLAUDE_API_KEY")
<<<<<<< HEAD
>>>>>>> e2bd6de (Moved call.py to app/servies folder for organisation)
=======
>>>>>>> 234e38c (Revert "Revert "Moved call.py to app/servies folder for organisation"")



# class LLMRequests(BaseModel):
#     queries: List[LLMRequest]

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e2bd6de (Moved call.py to app/servies folder for organisation)
=======
>>>>>>> 234e38c (Revert "Revert "Moved call.py to app/servies folder for organisation"")

def fetch_response(api_url, api_key, prompt):
    """Helper function to send API request to an LLM"""
    try:
        headers = {
            "Authorization": f"Bearer {api_key}"
        }

        response = requests.post(api_url, json={"prompt": prompt}, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
@router.post("/query")
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68bd2eb (file to handle LLM API requests)
=======
>>>>>>> 6e073d1 (Revert "Moved call.py to app/servies folder for organisation")
=======
db = {"queries": []}
@router.post("/query")
>>>>>>> 46ffaba (file to handle LLM API requests)
=======
db = {"queries": []}
@router.post("/query")
>>>>>>> d897b26 (Revert "Moved call.py to app/servies folder for organisation")
def queryLLM(request: LLMRequest):
    db["queries"].append(request)
    return {"message": f"Recieved query: {request.query}"}
=======
# @router.post("/prompt")
# def query_llm(request: LLMRequest):
#     """Handles incoming queries and sends them to multiple LLMs"""
    
#     responses = callChatBots(request.prompt)

#     return {"responses": responses}


#######################################

from flask import Flask, request, jsonify
import bcrypt
import os
import sys
import datetime
from dotenv import load_dotenv

# Add 'backend/llm' folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'llm')))

# Import LLM models
from llm.chatGPT import chatGPT
from llm.gemini import gemini
from llm.claude import claude
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
>>>>>>> 8d58dc2d74e74ec072fa5c5dd97a3ea680d3931c

    # Store responses in dictionary
    responses = {
        "chatgpt": {"response": chatgpt_response, "score": scores["chatgpt"]},
        "gemini": {"response": gemini_response, "score": scores["gemini"]},
        "claude": {"response": claude_response, "score": scores["claude"]}
    }

<<<<<<< HEAD
@router.get("/key")
def getKey():
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    return f"chatgpt: {chatGPTAPIKey}\ngemini: {geminiAPIKey}\nclaude: {claudeAPIKey}"
>>>>>>> d897b26 (Revert "Moved call.py to app/servies folder for organisation")
=======
    return {"responses": responses}
>>>>>>> 234e38c (Revert "Revert "Moved call.py to app/servies folder for organisation"")
=======
=======
@router.post("/prompt")
def query_llm(request: LLMRequest):
    """Handles incoming queries and sends them to multiple LLMs"""
>>>>>>> 9bf6d44 (returned deleted file to resolve rebase issue)
=======
# @router.post("/prompt")
# def query_llm(request: LLMRequest):
#     """Handles incoming queries and sends them to multiple LLMs"""
>>>>>>> e4f4d1c (Implemented flask code to fastapi)
    
#     responses = callChatBots(request.prompt)

#     return {"responses": responses}


#######################################

from flask import Flask, request, jsonify
import bcrypt
import os
import sys
import datetime
from dotenv import load_dotenv

# Add 'backend/llm' folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'llm')))

# Import LLM models
from llm.chatGPT import chatGPT
from llm.gemini import gemini
from llm.claude import claude
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
    
<<<<<<< HEAD
    # responses = {
    #     "Chatgpt": fetch_response("https://api.openai.com/v1/completions", chatGPTAPIKey, request.prompt),
    #     "Gemini": fetch_response("https://api.gemini.com/v1/completions", geminiAPIKey, request.prompt),
    #     "Claude": fetch_response("https://api.anthropic.com/v1/completions", claudeAPIKey, request.prompt),
    # }
    return {"responses": responses}
<<<<<<< HEAD
>>>>>>> ce9b745 (renamed services to llm and included all llm files in it)
=======
    return f"chatgpt: {chatGPTAPIKey}\ngemini: {geminiAPIKey}\nclaude: {claudeAPIKey}"
>>>>>>> 68bd2eb (file to handle LLM API requests)
=======
=======
>>>>>>> 53f5c11 (Revert "Revert "Moved call.py to app/servies folder for organisation"")
=======
@router.post("/query")
>>>>>>> e2bd6de (Moved call.py to app/servies folder for organisation)
=======
@router.post("/query")
>>>>>>> 234e38c (Revert "Revert "Moved call.py to app/servies folder for organisation"")
=======
@router.post("/prompt")
>>>>>>> abc2bdf (Removed some unused libraries and comments)
def query_llm(request: LLMRequest):
    """Handles incoming queries and sends them to multiple LLMs"""
<<<<<<< HEAD
    responses = {
        "Chatgpt": fetch_response("https://api.openai.com/v1/completions", chatGPTAPIKey, request.query),
        "Gemini": fetch_response("https://api.gemini.com/v1/completions", geminiAPIKey, request.query),
        "Claude": fetch_response("https://api.anthropic.com/v1/completions", claudeAPIKey, request.query),
    }
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    return {"responses": responses}
>>>>>>> 513022d (Moved call.py to app/servies folder for organisation)
=======
    return f"chatgpt: {chatGPTAPIKey}\ngemini: {geminiAPIKey}\nclaude: {claudeAPIKey}"
>>>>>>> 6e073d1 (Revert "Moved call.py to app/servies folder for organisation")
=======
    return {"responses": responses}
>>>>>>> 53f5c11 (Revert "Revert "Moved call.py to app/servies folder for organisation"")
=======
    return f"chatgpt: {chatGPTAPIKey}\ngemini: {geminiAPIKey}\nclaude: {claudeAPIKey}"
>>>>>>> 46ffaba (file to handle LLM API requests)
=======
    return {"responses": responses}
>>>>>>> e2bd6de (Moved call.py to app/servies folder for organisation)
=======
    return f"chatgpt: {chatGPTAPIKey}\ngemini: {geminiAPIKey}\nclaude: {claudeAPIKey}"
>>>>>>> d897b26 (Revert "Moved call.py to app/servies folder for organisation")
=======
    return {"responses": responses}
>>>>>>> 234e38c (Revert "Revert "Moved call.py to app/servies folder for organisation"")
=======
    
    responses = callChatBots(request.prompt)
    
    # responses = {
    #     "Chatgpt": fetch_response("https://api.openai.com/v1/completions", chatGPTAPIKey, request.prompt),
    #     "Gemini": fetch_response("https://api.gemini.com/v1/completions", geminiAPIKey, request.prompt),
    #     "Claude": fetch_response("https://api.anthropic.com/v1/completions", claudeAPIKey, request.prompt),
    # }
    return {"responses": responses}
>>>>>>> ce9b745 (renamed services to llm and included all llm files in it)
=======
>>>>>>> 9bf6d44 (returned deleted file to resolve rebase issue)
=======
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

=======
>>>>>>> 8d58dc2d74e74ec072fa5c5dd97a3ea680d3931c
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

# @app.route("/api/query", methods=["POST"])
# def query():
#     data = request.json
#     query_text = data.get("query", "")
#     response = chatGPT(query_text)
#     return jsonify({"response": response}), 200

# @app.route("/add_test_data", methods=["POST"])
# def add_test_data():
#     test_data = {
#         "email": "testuser@example.com",
#         "question": "What is the capital of France?",
#         "response": "Paris",
#         "timestamp": datetime.datetime.now(datetime.timezone.utc)
#     }
#     db.collection("submissions").add(test_data)
#     return jsonify({"message": "Test data added successfully!"}), 200

def score_response(response):
    return len(response)  # Simple example: longer responses score higher




#######################################
<<<<<<< HEAD
>>>>>>> e4f4d1c (Implemented flask code to fastapi)
=======
>>>>>>> 8d58dc2d74e74ec072fa5c5dd97a3ea680d3931c
