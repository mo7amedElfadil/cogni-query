import os
import uuid
from celery import Celery
from pymongo import MongoClient
from qdrant_client import QdrantClient, models
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import fitz  # PyMuPDF

# --- Configuration ---
REDIS_URL = os.environ.get("REDIS_URL", "redis://redis:6379/0")
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://mongo:27017")
QDRANT_URL = os.environ.get("QDRANT_URL", "http://qdrant:6333")
QDRANT_COLLECTION_NAME = "pdf_chunks"

# --- Clients ---
celery_app = Celery('tasks', broker=REDIS_URL, backend=REDIS_URL)
mongo_client = MongoClient(MONGO_URI)
db = mongo_client.cogni_query
qdrant_client = QdrantClient(url=QDRANT_URL)

# --- Models ---
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# --- Text Splitter ---
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len
)

# --- Qdrant Collection Setup ---
try:
    qdrant_client.recreate_collection(
        collection_name=QDRANT_COLLECTION_NAME,
        vectors_config=models.VectorParams(size=embedding_model.get_sentence_embedding_dimension(), distance=models.Distance.COSINE),
    )
except Exception as e:
    print(f"Qdrant collection already exists or another error occurred: {e}")


@celery_app.task(name="process_pdf")
def process_pdf(document_id: str, file_path: str):
    """
    Celery task to process a PDF file.
    """
    documents_collection = db.documents

    try:
        # 1. Update status to 'processing'
        documents_collection.update_one({"_id": document_id}, {"$set": {"status": "processing"}})

        # 2. Extract text from PDF
        doc = fitz.open(file_path)
        chunks = []
        for page_num, page in enumerate(doc):
            text = page.get_text()
            if text:
                page_chunks = text_splitter.split_text(text)
                for chunk in page_chunks:
                    chunks.append({
                        "text": chunk,
                        "page_number": page_num + 1
                    })
        doc.close()

        if not chunks:
            documents_collection.update_one({"_id": document_id}, {"$set": {"status": "failed", "error": "No text could be extracted."}})
            return

        # 3. Generate embeddings
        embeddings = embedding_model.encode([chunk["text"] for chunk in chunks])

        # 4. Store in Qdrant
        qdrant_client.upsert(
            collection_name=QDRANT_COLLECTION_NAME,
            points=[
                models.PointStruct(
                    id=str(uuid.uuid4()),
                    vector=embedding.tolist(),
                    payload={
                        "text_chunk": chunk["text"],
                        "document_id": document_id,
                        "page_number": chunk["page_number"]
                    }
                )
                for i, (chunk, embedding) in enumerate(zip(chunks, embeddings))
            ]
        )

        # 5. Update status to 'completed'
        documents_collection.update_one({"_id": document_id}, {"$set": {"status": "completed"}})

    except Exception as e:
        documents_collection.update_one({"_id": document_id}, {"$set": {"status": "failed", "error": str(e)}})
        print(f"Error processing document {document_id}: {e}")

    finally:
        # Clean up the temporary file
        if os.path.exists(file_path):
            os.remove(file_path)
