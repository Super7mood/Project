import os
import firebase_admin
from firebase_admin import credentials, firestore

# Load Firebase Service Account Key
cred = credentials.Certificate("serviceAccountKey.json")

firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

# Collections
responses_collection = db.collection("ai_responses")  # AI responses collection
users_collection = db.collection("users")  # Users collection

print("✅ Connected to Firestore")
