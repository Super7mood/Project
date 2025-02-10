from flask import Flask, request, jsonify
import bcrypt
import os
import sys
import datetime
from dotenv import load_dotenv

# Add the 'backend/llm' folder to the Python path explicitly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'llm')))

# Import LLM models after modifying the path
from llm.chatGPT import chatGPT
from llm.gemini import gemini
from llm.claude import claude

from flask_cors import CORS

# 🔹 Firestore Setup
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load environment variables from .env
load_dotenv()

# Initialize Firebase using the JSON key
cred = credentials.Certificate("firebase-adminsdk.json")  # Ensure this matches your file name
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

@app.route("/")
def home():
    return "<h1>Welcome to AI Checker Pro API</h1><p>Use the API endpoints to interact with the system.</p>"

# ================================
# 🔹 USER REGISTRATION (Firestore)
# ================================
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
        "password": hashed_password.decode('utf-8'),
        "created_at": datetime.datetime.utcnow()
    })

    return jsonify({"message": "User registered successfully!"}), 200


# ================================
# 🔹 USER LOGIN (Firestore)
# ================================
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


# ================================
# 🔹 QUESTION SUBMISSION (Firestore)
# ================================
@app.route("/ask", methods=["POST"])
def ask_question():
    data = request.json
    email = data["email"]
    question = data["question"]

    # Get responses from each LLM model
    chatgpt_response = chatGPT(question)
    gemini_response = gemini(question)
    claude_response = claude(question)

    # Store the question and responses in Firestore
    db.collection("submissions").add({
        "user_email": email,
        "question": question,
        "chatgpt_response": chatgpt_response,
        "gemini_response": gemini_response,
        "claude_response": claude_response,
        "timestamp": datetime.datetime.utcnow()
    })

    return jsonify({
        "chatgpt_response": chatgpt_response,
        "gemini_response": gemini_response,
        "claude_response": claude_response
    }), 200

# ================================
# 🔹 API QUERY ENDPOINT
# ================================
@app.route("/api/query", methods=["POST"])
def query():
    data = request.json
    query_text = data.get("query", "")

    # Example: Using chatGPT model to process the query
    response = chatGPT(query_text)

    return jsonify({"response": response}), 200

# ================================
# 🔹 ADD TEST DATA TO FIRESTORE
# ================================
@app.route("/add_test_data", methods=["POST"])
def add_test_data():
    test_data = {
        "email": "testuser@example.com",
        "question": "What is the capital of France?",
        "response": "Paris",
        "timestamp": datetime.datetime.utcnow()
    }
    db.collection("submissions").add(test_data)
    return jsonify({"message": "Test data added successfully!"}), 200

# ================================
# 🔹 RUN FLASK APP
# ================================
if __name__ == "__main__":
    app.run(debug=True)
