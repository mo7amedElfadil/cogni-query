from celery import Celery
import os
from pymongo import MongoClient
from datetime import datetime

# --- Configuration ---
REDIS_URL = "redis://redis:6379/0"
MONGO_URI = "mongodb://mongo:27017"

# --- Clients ---
celery_app = Celery('tasks', broker=REDIS_URL)
mongo_client = MongoClient(MONGO_URI)
db = mongo_client.cogni_query
documents_collection = db.documents

# --- Test Data ---
# Create a dummy PDF file for testing
pdf_content = b"%PDF-1.4\n1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n3 0 obj\n<< /Type /Page /Parent 2 0 R /Resources <<>> /MediaBox [0 0 612 792] /Contents 4 0 R >>\nendobj\n4 0 obj\n<< /Length 52 >>\nstream\nBT\n/F1 24 Tf\n100 700 Td\n(This is a test PDF.) Tj\nET\nendstream\nendobj\nxref\n0 5\n0000000000 65535 f \n0000000010 00000 n \n0000000059 00000 n \n0000000112 00000 n \n0000000212 00000 n \ntrailer\n<< /Size 5 /Root 1 0 R >>\nstartxref\n309\n%%EOF"
file_path = "/app/shared_files/test.pdf"
# This path is inside the container, so we need to write to the mounted volume
host_file_path = "shared_files/test.pdf"
with open(host_file_path, "wb") as f:
    f.write(pdf_content)

# --- Create Document in MongoDB ---
document_id = "test_document_123"
documents_collection.insert_one({
    "_id": document_id,
    "user_id": "test_user",
    "filename": "test.pdf",
    "upload_date": datetime.utcnow(),
    "status": "uploaded"
})

# --- Enqueue Task ---
celery_app.send_task('process_pdf', args=[document_id, file_path])

print(f"Task to process '{file_path}' for document_id '{document_id}' has been sent to the queue.")
