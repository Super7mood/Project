import os
import pymongo
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get MongoDB URI from .env
MONGO_URI = os.getenv("MONGO_URI")

# Connect to MongoDB Atlas
client = pymongo.MongoClient(MONGO_URI)
db = client["aicheckerpro"]  # Make sure the database is named 'aicheckerpro'
responses_collection = db["ai_responses"]  # Collection for storing AI responses
users_collection = db["users"]  # Collection for storing users

print("✅ Connected to MongoDB Atlas")
