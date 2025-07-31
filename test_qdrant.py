from qdrant_client import QdrantClient

# --- Configuration ---
QDRANT_URL = "http://localhost:6333"
QDRANT_COLLECTION_NAME = "pdf_chunks"

# --- Client ---
qdrant_client = QdrantClient(url=QDRANT_URL)

# --- Get Collection Info ---
collection_info = qdrant_client.get_collection(collection_name=QDRANT_COLLECTION_NAME)
print(collection_info)

# --- Count Points ---
count_result = qdrant_client.count(
    collection_name=QDRANT_COLLECTION_NAME,
    exact=True
)
print(count_result)
