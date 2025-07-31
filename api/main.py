from fastapi import FastAPI, HTTPException, UploadFile, File
from pymongo import MongoClient
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from cryptography.fernet import Fernet
import os
import shutil
from celery import Celery

# --- Configuration ---
MONGO_URI = "mongodb://mongo:27017"
REDIS_URL = "redis://redis:6379/0"
SHARED_FILES_PATH = "/app/shared_files"

# --- Clients ---
client = MongoClient(MONGO_URI)
db = client.cogni_query
celery_app = Celery('tasks', broker=REDIS_URL)


# --- Encryption ---
# NOTE: In a real application, this key should be loaded securely, e.g., from an environment variable
SECRET_KEY = Fernet.generate_key()
fernet = Fernet(SECRET_KEY)

def encrypt_key(key: str) -> bytes:
    return fernet.encrypt(key.encode())

def decrypt_key(encrypted_key: bytes) -> str:
    return fernet.decrypt(encrypted_key).decode()

# --- Pydantic Models ---
class ApiKey(BaseModel):
    user_id: str
    service: str  # e.g., "openai", "gemini"
    key: str

class UserSettings(BaseModel):
    id: str = Field(..., alias="_id")
    user_id: str
    api_keys: dict = {}

# --- FastAPI App ---
app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(MONGO_URI)
    app.database = app.mongodb_client.cogni_query
    if not os.path.exists(SHARED_FILES_PATH):
        os.makedirs(SHARED_FILES_PATH)
    print("Connected to the MongoDB database!")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to Cogni-Query API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/api/v1/keys", status_code=201)
def save_api_key(api_key: ApiKey):
    user_settings_collection = app.database.user_settings
    
    # Encrypt the key before storing
    encrypted_key = encrypt_key(api_key.key)
    
    # Find user settings or create new one
    user_settings = user_settings_collection.find_one({"user_id": api_key.user_id})
    
    if user_settings:
        # Update existing settings
        user_settings["api_keys"][api_key.service] = encrypted_key
        user_settings_collection.update_one(
            {"user_id": api_key.user_id},
            {"$set": {"api_keys": user_settings["api_keys"]}}
        )
    else:
        # Create new settings
        new_settings = {
            "user_id": api_key.user_id,
            "api_keys": {
                api_key.service: encrypted_key
            }
        }
        user_settings_collection.insert_one(new_settings)
        
    return {"message": f"API key for {api_key.service} saved successfully."}

@app.post("/api/v1/documents/upload", status_code=201)
async def upload_documents(files: List[UploadFile] = File(...), user_id: str = "test_user"):
    documents_collection = app.database.documents
    uploaded_documents = []

    for file in files:
        # Save file to shared volume
        file_path = os.path.join(SHARED_FILES_PATH, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Create document record in MongoDB
        document_data = {
            "user_id": user_id,
            "filename": file.filename,
            "upload_date": datetime.utcnow(),
            "status": "uploaded"
        }
        result = documents_collection.insert_one(document_data)
        document_id = result.inserted_id

        # Dispatch Celery task
        celery_app.send_task('process_pdf', args=[str(document_id), file_path])

        uploaded_documents.append({
            "document_id": str(document_id),
            "filename": file.filename,
            "status": "processing"
        })

    return {"uploaded_documents": uploaded_documents}