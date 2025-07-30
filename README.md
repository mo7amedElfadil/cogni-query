# **Cogni-Query: Product Requirements and Technical Specification Document (PRD)**

## **Section 1: Project Vision and System Overview**

This section outlines the strategic vision, core functionality, and target audience for the Cogni-Query platform. It establishes the foundational requirements that will guide the architectural and implementation decisions detailed in subsequent sections.

### **1.1. Executive Summary: The "Cogni-Query" Platform**

### **1.1.1. Product Definition**

Cogni-Query is an interactive, AI-powered document intelligence platform engineered for professionals and academics who must navigate and synthesize vast amounts of information. The system is designed to ingest large collections of PDF documents in batch and transform them from static, siloed files into a unified, dynamic, and conversational knowledge base. It serves as a sophisticated research assistant, enabling users to pose complex questions in natural language and receive contextually accurate, source-grounded answers derived directly from their document corpus.

The platform distinguishes itself by providing users with direct control over the AI engine, allowing them to select their preferred Large Language Model (LLM) provider—initially supporting Gemini and OpenAI—and utilize their own API keys. This approach offers unparalleled flexibility, transparency, and cost management, empowering users to leverage the full potential of state-of-the-art language models on their private data sets.

### **1.1.2. Core Value Proposition**

The primary value of the Cogni-Query platform lies in its ability to overcome the fundamental limitations of standard LLM interactions, namely the constrained context window (token limits). By implementing an advanced Retrieval-Augmented Generation (RAG) architecture, the platform empowers users to "chat with their documents" at a scale previously unattainable through simple copy-paste methods. Users can analyze hundreds or even thousands of pages of text simultaneously, extracting key insights, verifying information, and discovering connections without the laborious process of manual reading and searching. This transforms weeks of manual review into minutes of interactive discovery.

This core capability directly addresses a critical pain point for knowledge workers across various domains. The platform's emphasis on user-provided API keys further enhances its value proposition by placing cost control and model choice directly in the hands of the user, a significant differentiator from many closed-system competitors that bundle AI costs into a subscription fee.

### **1.1.3. Target User Personas**

The platform is designed to serve a diverse set of user personas whose work is fundamentally centered on document analysis and information synthesis.

- **The Academic Researcher:** This user is often tasked with conducting comprehensive literature reviews, which involves analyzing hundreds of academic papers. Cogni-Query enables them to quickly identify research trends, compare methodologies across papers, and extract specific data points, significantly accelerating the research lifecycle. This aligns with the functionality offered by specialized academic tools like Paperguide and Elicit.
- **The Legal Professional:** Attorneys, paralegals, and legal researchers frequently review voluminous discovery documents, case law, and contracts. The platform provides a secure environment to upload these sensitive documents and rapidly query for specific clauses, precedents, or factual statements, complete with citations to the exact source page, thereby enhancing due diligence and case preparation.
- **The Financial Analyst:** This user must distill actionable intelligence from a wide array of financial reports, SEC filings, and market analyses. Cogni-Query allows them to batch-process these documents and ask targeted questions about financial metrics, risk factors, or management discussions, streamlining the process of data extraction and analysis.
- **The Student:** Graduate and undergraduate students can use the platform to study from multiple textbooks, research articles, and lecture notes. It facilitates a deeper understanding of complex topics by allowing them to ask clarifying questions and receive synthesized answers drawn from their entire library of course materials.

### **1.2. Core User Epics and Functional Requirements**

The following user epics define the high-level functionality of the Cogni-Query platform for its initial release (V1).

- **1.2.1. User Authentication & Onboarding:**
    - As a new user, I can create a secure account using my email and a password.
    - As a registered user, I can log in to the platform to access my workspace.
    - As a logged-in user, I can navigate to a settings page where I can securely add, update, and remove my API keys for supported LLM providers (e.g., OpenAI, Gemini). The system must ensure these keys are stored securely and are never exposed on the client side.
- **1.2.2. Document Management:**
    - As a user, I can create distinct "Projects" or "Collections" to organize my documents for different analysis tasks.
    - As a user, I can select a project and upload multiple PDF documents simultaneously in a single batch operation.
    - As a user, I can view the status of my uploaded documents (e.g., "Pending," "Processing," "Completed," "Failed") in the UI.
    - As a user, I can view a list of all documents within a project and have the option to delete them.
- **1.2.3. Interactive Analysis:**
    - As a user, I can select a project and open an interactive chat interface.
    - As a user, I can type a question in natural language into the chat input.
    - As a user, I will receive a synthesized answer from the AI that is based on the content of the documents within that project.
    - As a user, I can see clear citations within or alongside the AI's response, indicating which document and page number the information was sourced from, allowing for easy verification.
    - As a user, I can ask follow-up questions, and the AI will understand the context of the ongoing conversation.
- **1.2.4. LLM Provider Selection:**
    - As a user, before or during a chat session, I can select which of my configured LLM providers (e.g., "OpenAI - gpt-4o," "Gemini - 1.5 Pro") I want to use for generating responses.
    - The system will use the selected provider for all subsequent queries in that session until I change it again.

### **1.3. Differentiators and Feature Roadmap (V1 Scope)**

To ensure a successful and focused initial launch, the scope of Version 1.0 will be strictly defined. The development effort will concentrate on delivering a robust and polished core user experience, establishing a strong foundation for future enhancements.

- **V1 Focus:** The singular focus of the V1 release is to perfect the core user workflow: **Batch Upload -> Asynchronous Processing (RAG Pipeline) -> Interactive, Source-Cited Chat**. This includes the secure management of user-provided API keys and the choice of LLM provider. The user interface will be clean, intuitive, and centered entirely on this workflow.
- **Key Differentiator:** The primary market differentiator for V1 will be the combination of three key features:
    1. A robust, scalable RAG implementation that genuinely removes token limitations for large document sets.
    2. The flexibility for users to bring their own API keys, providing direct control over costs and access to the latest models.
    3. A highly responsive and interactive chat experience with verifiable, source-grounded answers.
- **Future Considerations (Post-V1 Roadmap):** While not in scope for the initial release, the system's architecture will be designed to accommodate future features inspired by advanced functionalities seen in market-leading tools. This ensures the platform can evolve without requiring a complete architectural overhaul. Potential future features include:
    - **Structured Data Extraction:** Automatically identifying and extracting tabular data from PDFs into a structured, downloadable format (e.g., CSV, Excel), similar to features in Parabola and Elicit.
    - **Advanced Analysis Reports:** Generating comprehensive reports that summarize key themes, identify research trends, and highlight contradictions or consensus across the entire document collection.
    - **Reference Manager Integration:** Allowing users to import documents directly from and export citations to reference management software like Zotero or EndNote.
    - **Multimodal Support:** Expanding beyond PDFs to include other document formats (e.g., DOCX, HTML) and eventually incorporating analysis of images and tables within documents.

The deliberate decision to narrow the V1 scope is critical. The user's request outlines a complex, full-stack application with advanced AI at its core. Attempting to match the feature set of mature competitors like Paperguide  or Elicit  from the outset would introduce significant risk, potentially leading to a product that does many things poorly rather than one thing exceptionally well. By focusing on the most unique and challenging aspects of the user's request—the scalable RAG pipeline and user-managed API keys—V1 of Cogni-Query will deliver immediate, tangible value and establish a solid market foothold.

---

## **Section 2: System Architecture and Technology Stack Rationale**

This section presents the architectural blueprint for the Cogni-Query platform. The design prioritizes scalability, maintainability, security, and performance by adopting a microservices-based approach and selecting best-in-class technologies for each component of the system. Each technological choice is rigorously justified based on industry best practices and the specific requirements of the application.

### **2.1. The Microservices-Based Architectural Blueprint**

A monolithic architecture, where all functionality is contained within a single application, is ill-suited for the demands of Cogni-Query. The system involves both fast, lightweight user interactions (like API requests) and slow, computationally intensive background processes (like PDF analysis and embedding). A microservices architecture provides the necessary separation of concerns, allowing each part of the system to be developed, deployed, and scaled independently.

### **2.1.1. High-Level Architecture Overview**

The platform will be composed of a set of loosely coupled services that communicate through well-defined APIs and a central message broker. This design ensures that a spike in document processing load does not impact the responsiveness of the user-facing application.

The primary services and their interactions are as follows:

1. The **Frontend Service** (user's browser) communicates exclusively with the **API Gateway**.
2. The **API Gateway** authenticates requests and routes them to the appropriate backend service. For long-running tasks like document ingestion, it places a job onto a message queue.
3. The **Ingestion Service**, implemented as a set of Celery workers, picks up jobs from the message queue and performs the heavy lifting of PDF processing and embedding.
4. The **Chat Service** handles the real-time RAG logic, querying the databases and interacting with the external LLM APIs.
5. All services interact with the **Database Layer** and **Message Broker** as needed.

### **2.1.2. Core Services**

- **Frontend Service (React with Next.js):** A Single-Page Application (SPA) that provides the entire user interface. It is responsible for rendering the document management dashboard, the chat interface, and the user settings panel.
- **API Gateway (Python with FastAPI):** The sole entry point for all requests originating from the frontend. Its responsibilities include:
    - User authentication and session management.
    - Validating incoming requests.
    - Routing synchronous requests (e.g., get conversation history) to the Chat Service.
    - Dispatching asynchronous tasks (e.g., process new document) to the Ingestion Service via the message broker.
- **Ingestion Service (Python with Celery):** A set of background workers that operate independently of the API Gateway. This service is responsible for the entire document processing pipeline:
    - Consuming "process document" tasks from the queue.
    - Extracting text from PDFs (including OCR).
    - Cleaning and chunking the text.
    - Generating vector embeddings for each chunk.
    - Indexing the chunks in the vector database.
    - Updating the document's status in the metadata database.
- **Chat Service (Python with FastAPI):** A dedicated service that manages the conversational AI logic. Its responsibilities include:
    - Receiving user queries from the API Gateway.
    - Orchestrating the RAG pipeline: embedding the query, retrieving relevant chunks from the vector database, and constructing the final prompt.
    - Interacting with the selected external LLM API (OpenAI or Gemini).
    - Streaming the AI-generated response back to the user.
    - Persisting the conversation history.

### **2.1.3. Supporting Infrastructure**

- **Databases (Hybrid: MongoDB & Qdrant):** A dual-database strategy is employed to leverage the strengths of different database technologies. MongoDB will serve as the primary metadata store, while Qdrant will be the specialized vector database for semantic search.
- **Message Broker (Redis):** Redis will serve as the high-speed, in-memory message broker for Celery, facilitating the communication between the API Gateway and the Ingestion Service workers.
- **Cache (Redis):** Redis will also be used as a general-purpose cache to store session data and the results of frequently executed queries, reducing database load and improving response times.

### **2.2. Recommended Technology Stack & Justification**

The selection of the technology stack is driven by the goal of building a high-performance, scalable, and maintainable AI application. The user's proposed stack of Python, React, and MongoDB serves as an excellent foundation, which is refined here with more specialized components to create an optimal solution.

### **2.2.1. Backend Framework: Python with FastAPI**

- **Rationale:** Python is the de facto standard for AI and Machine Learning development, offering an unparalleled ecosystem of libraries such as `Hugging Face Transformers`, `PyTorch`, `LangChain`, and clients for every major AI API. This makes it the only logical choice for the backend services that will interact with LLMs and embedding models. While traditional Python web frameworks can be slow, modern asynchronous frameworks mitigate this issue. FastAPI is selected over alternatives like Django or Flask because it is built for high-performance, asynchronous I/O, which is crucial for handling concurrent API requests and streaming responses. Its use of Python type hints and Pydantic for data validation leads to more robust, self-documenting code, which is essential for a microservices architecture.

### **2.2.2. Frontend Framework: React with Next.js**

- **Rationale:** React is a mature and powerful library for building complex and interactive user interfaces. Its component-based architecture is well-suited for developing the modular UI elements required for Cogni-Query, such as the chat window and document list. The decision to use Next.js as the framework built upon React is strategic. Next.js provides out-of-the-box support for server-side rendering (SSR) and static site generation (SSG), which can lead to significantly faster initial page load times and improved SEO performance compared to a client-side-only React app. It also offers a simplified routing system and an opinionated project structure that encourages best practices, accelerating development.

### **2.2.3. Database Strategy: Hybrid MongoDB & Qdrant**

- **Rationale:** To achieve maximum performance and scalability, a specialized, hybrid database approach is necessary.
    - **MongoDB:** The user's requirement for MongoDB is well-founded. As a leading NoSQL document database, it excels at storing flexible, semi-structured data. It is the ideal choice for managing `users`, `documents`, and `conversations` collections, where the schema may evolve and data structures can be complex (e.g., nested message arrays). Its horizontal scalability ensures it can handle a growing user base and large volumes of metadata.
    - **Qdrant:** While MongoDB offers vector search capabilities, a dedicated vector database is purpose-built and optimized for the high-speed similarity searches that are the cornerstone of the RAG pipeline. Qdrant is a powerful, open-source vector database known for its high performance, advanced filtering capabilities (e.g., filtering by `user_id` or `document_id` before searching), and efficient memory usage through quantization. Separating the vector index into Qdrant allows the RAG system to perform its core function with minimal latency, without burdening the primary metadata database. This separation of concerns is a critical architectural decision for building a high-performance AI system.

### **2.2.4. Asynchronous Task Queue: Celery with Redis**

- **Rationale:** The process of ingesting a PDF—extracting text, performing OCR on scanned pages, chunking the content, and generating embeddings for hundreds of chunks—is a long-running and resource-intensive operation. Performing this task synchronously within an API request would result in unacceptable client timeouts and a poor user experience. Celery is the industry-standard distributed task queue for Python, designed explicitly to offload such tasks to background workers. This decouples the responsive API from the heavy processing, allowing the system to scale the number of workers independently based on the ingestion load. Redis is chosen as the message broker and result backend for Celery due to its exceptional speed, low latency, and simplicity, making it a perfect fit for a high-throughput task queueing system.

---

## **Section 3: The Retrieval-Augmented Generation (RAG) Pipeline: Implementation Deep Dive**

This section provides a detailed, step-by-step technical specification for the core AI engine of the Cogni-Query platform. This RAG pipeline is designed to handle large volumes of text efficiently, overcoming the context window limitations of LLMs and enabling a rich, contextual chat experience.

### **3.1. Stage 1: The Ingestion and Processing Service (Celery Worker)**

The ingestion process begins the moment a user uploads documents. It is handled entirely by asynchronous Celery workers to ensure the main application remains responsive.

### **3.1.1. Triggering the Ingestion Task**

When a user uploads one or more PDFs, the API Gateway performs the following actions:

1. Receives the file(s) and streams them to a temporary, secure storage location (e.g., a local volume or an S3-compatible object store).
2. For each file, it creates a new document record in the MongoDB `documents` collection. This record includes the `user_id`, `filename`, `storage_path`, and an initial `status` of `"PENDING"`.
3. For each new document record, it dispatches a task to the Celery message queue (Redis). The task message contains the `document_id` from MongoDB, which the worker will use to retrieve all necessary information.

### **3.1.2. PDF Text Extraction**

The Celery worker, upon receiving a task, will fetch the document's metadata from MongoDB and retrieve the PDF file from storage. It will then employ a two-stage text extraction strategy to handle both searchable and image-based (scanned) PDFs.

1. **Primary Method (Searchable PDFs):** The worker will first attempt to extract text using a high-performance Python library like `pdfium2` or `PyPDF2`. These libraries parse the internal structure of the PDF to extract text directly, which is fast and highly accurate for digitally-native documents.
2. **Fallback Method (Scanned PDFs):** If the primary method yields little or no text, the worker will infer that the document is scanned or image-based. It will then pivot to an Optical Character Recognition (OCR) process. For this, a locally-hosted, open-source OCR engine is recommended to maintain user privacy and control costs. The **Kreuzberg** library, which leverages the powerful Tesseract OCR engine, is an excellent choice as it provides a unified interface for both searchable and scanned documents and runs entirely locally. Another strong alternative is
    
    **olmOCR**, which is specifically trained on academic and technical documents for high accuracy. This local processing approach deliberately avoids dependencies on paid cloud services like AWS Textract or Azure Document Intelligence for the V1 implementation.
    

### **3.1.3. Text Cleaning and Pre-processing**

The raw extracted text is often noisy and requires cleaning to ensure high-quality embeddings. The worker will perform a series of cleaning steps based on established best practices for RAG data preparation :

- Remove excessive whitespace, including multiple spaces, tabs, and redundant line breaks.
- Normalize Unicode characters to a standard form.
- Optionally, implement logic to identify and remove common headers, footers, and page numbers that add little semantic value.
- Correct common OCR errors if possible, using simple pattern-based replacements.

### **3.1.4. Document Chunking**

This is the most critical step for overcoming LLM token limits. The cleaned text is segmented into smaller, contextually coherent pieces. The choice of chunking strategy significantly impacts the quality of the retrieval process.

- **Chunking Strategy:** The system will implement **Recursive Character Text Splitting**. This strategy is superior to fixed-size chunking because it is adaptive. It attempts to split text along a prioritized list of separators (e.g., `"\n\n"` for paragraphs, then `"\n"` for lines, then `". "` for sentences), which helps to keep semantically related content within the same chunk.
- **Chunking Parameters:**
    - `chunk_size`: A target size of **1024 tokens** will be used. This size is large enough to contain meaningful context but small enough to be efficiently processed by embedding models and LLMs.
    - `chunk_overlap`: An overlap of **100-200 tokens** will be configured. This ensures that sentences or ideas are not abruptly cut off at chunk boundaries, maintaining contextual continuity between adjacent chunks.
- **Metadata Association:** Each generated chunk will be stored along with critical metadata that will be indexed in the vector database. This metadata includes the `document_id` of its source file, the `page_number` where the chunk begins, and its sequential `chunk_index` within the document.

### **3.2. Stage 2: The Embedding and Indexing Pipeline (Celery Worker)**

After chunking, the same Celery worker proceeds to convert the text chunks into numerical representations (embeddings) and index them for fast retrieval.

### **3.2.1. Embedding Model Selection**

The quality of the embeddings directly determines the quality of the semantic search. The platform will be architected to support multiple embedding models, but will launch with well-chosen defaults.

- **Default Proprietary Model:** **OpenAI `text-embedding-3-small`**. This model is selected for its excellent balance of high performance on retrieval benchmarks, relatively low cost, and ease of use. It is a strong default choice for production RAG systems.
- **Default Open-Source Model:** **BAAI `bge-large-en-v1.5`**. This model is consistently ranked at the top of the Hugging Face MTEB (Massive Text Embedding Benchmark) leaderboard for retrieval tasks. Offering it as an option allows users who prefer not to use a proprietary service or who wish to self-host to still have access to state-of-the-art embedding quality.

The system's embedding logic will be built using an adapter pattern, making it straightforward to add support for other models like those from Cohere or Google Vertex AI in the future.

### **Table 3.2.1: Comparison of Recommended Embedding Models**

| Model Name | Provider/Source | Key Strengths | Cost (per 1M tokens) | Dimensionality | Recommended Use Case |
| --- | --- | --- | --- | --- | --- |
| `text-embedding-3-small` | OpenAI | Excellent cost-performance balance, industry standard for RAG. | ~$0.02 | 1536 | Default for general-purpose, high-quality document analysis. |
| `text-embedding-3-large` | OpenAI | Highest performance proprietary model, state-of-the-art recall. | ~$0.13 | 3072 | Projects requiring maximum retrieval accuracy where cost is secondary. |
| `bge-large-en-v1.5` | BAAI (Open Source) | Top-tier open-source performance, self-hostable for privacy/cost control. | Free (requires hosting) | 1024 | Advanced users who want to avoid proprietary APIs or have specific hosting requirements. |
| `embed-english-v3.0` | Cohere | High performance, options for compression-aware training. | ~$0.10 | 1024 | Enterprise search and applications where Cohere's ecosystem is already in use. |
| `nomic-embed-text-v1.5` | Nomic (Open Source) | Excellent performance with a large 8192 token context length. | Free (requires hosting) | 768 | Analyzing documents with very long, unbroken paragraphs or sections. |

### **3.2.2. Generating and Indexing Embeddings**

The worker will perform the following steps:

1. Group the text chunks into batches to make efficient calls to the embedding model's API.
2. For each batch, send the text to the selected embedding model (e.g., OpenAI API) and receive the corresponding vector embeddings.
3. As embeddings are generated, the worker will "upsert" them into the **Qdrant** vector database. Each point in Qdrant will consist of:
    - A unique ID (e.g., a UUID).
    - The high-dimensional vector.
    - A payload containing the associated metadata: the raw `text` of the chunk, `document_id`, `user_id`, `page_number`, and `chunk_index`.
4. Once all chunks for a document are successfully indexed, the worker updates the document's status in the MongoDB `documents` collection to `"COMPLETED"`. If any step fails, the status is set to `"FAILED"` with an error message.

### **3.3. Stage 3: The Retrieval and Synthesis Engine (Chat Service)**

This stage is executed in real-time when a user interacts with the chat interface. It is handled by the dedicated Chat Service.

### **3.3.1. Query Processing and Retrieval**

1. The Chat Service receives the user's question and the `conversation_id` from the API Gateway.
2. It uses the same embedding model that was used for the documents in that conversation to generate a vector embedding for the user's query.
3. It then performs a similarity search against the Qdrant `document_chunks` collection. The search query includes:
    - The user's query vector.
    - A `top_k` parameter (e.g., `k=5`) to retrieve the 5 most relevant chunks.
    - A metadata filter to ensure it only searches within the `document_ids` associated with the current conversation. This is crucial for data isolation and relevance.

### **3.3.2. Prompt Engineering and Synthesis**

After retrieving the most relevant chunks, the service constructs a carefully engineered prompt to send to the selected LLM (Gemini or OpenAI). This prompt engineering is vital for ensuring the LLM provides accurate, grounded, and citable answers.

- **Structured Prompt Template:** The prompt will follow a strict structure:
    
    `System Prompt:
    You are an expert research assistant named Cogni-Query. Your task is to answer the user's question based *exclusively* on the provided context extracted from their documents. Do not use any external knowledge. If the answer is not contained within the provided context, you must state that the information is not available in the documents. When you use information from the context to form your answer, you MUST cite the source using the format.
    
    Provided Context:
    ---
    Context 1:
    Source Document: financial_report_q3.pdf
    Source Page: 12
    Content:
    "The company's net revenue increased by 15% year-over-year, driven primarily by strong performance in the North American market."
    ---
    Context 2:
    Source Document: market_analysis_2024.pdf
    Source Page: 45
    Content:
    "Despite overall market headwinds, the consumer electronics sector showed resilience, with our primary competitor reporting a 10% growth."
    ---
    (Additional retrieved contexts would be included here)
    
    Conversation History:
    User: What was the revenue growth last quarter?
    Assistant: The company's net revenue increased by 15% year-over-year.
    
    User Question:
    How did that compare to competitors?`
    

This structured approach, which includes a clear role, strict instructions, the retrieved context with metadata, and the recent conversation history, guides the LLM to synthesize a high-quality response that directly addresses the user's needs for accuracy and verifiability.

### **3.3.3. Streaming Response**

The Chat Service will make the API call to the chosen LLM with the `stream=True` option. This allows the service to receive the response token by token. It will then immediately forward these tokens to the frontend via a streaming HTTP response. This results in the AI's answer appearing character-by-character in the UI, providing immediate feedback to the user and greatly enhancing the perceived performance of the application.

---

## **Section 4: Data Modeling and Database Schemas**

This section defines the precise data structures for both the MongoDB metadata store and the Qdrant vector database. The schemas are designed for scalability, data integrity, and efficient querying, reflecting best practices for modern AI and chat applications.

### **4.1. MongoDB Collection Schemas**

The MongoDB database will house all non-vector data, including user information, document metadata, and conversation logs. The design employs a referencing pattern over an embedding pattern for chat messages to prevent documents from exceeding MongoDB's 16MB size limit and to ensure scalability, a critical consideration for applications with potentially long conversation histories.

### **4.1.1. `users` Collection**

This collection stores essential user account information and their securely encrypted API keys.

**Table 4.1.1: `users` Collection Schema**

| Field Name | Data Type | Description |
| --- | --- | --- |
| `_id` | `ObjectId` | Auto-generated unique identifier and primary key. |
| `email` | `String` | User's email address. Must be unique and is indexed for fast lookups. |
| `password_hash` | `String` | Hashed and salted password for secure authentication. Plaintext passwords are never stored. |
| `created_at` | `Timestamp` | Timestamp of when the user account was created. |
| `api_keys` | `Array` | An array of embedded documents, each representing a user-provided API key. |
| `api_keys.provider` | `String` | The name of the LLM provider (e.g., "openai", "gemini"). |
| `api_keys.encrypted_key` | `Binary` | The user's API key, symmetrically encrypted. This is stored as binary data. |
| `api_keys.added_at` | `Timestamp` | Timestamp of when the key was added or last updated. |

Export to Sheets

### **4.1.2. `documents` Collection**

This collection serves as a catalog for every PDF file uploaded by users, tracking its metadata and processing status.

**Table 4.1.2: `documents` Collection Schema**

| Field Name | Data Type | Description |
| --- | --- | --- |
| `_id` | `ObjectId` | Auto-generated unique identifier and primary key. |
| `user_id` | `ObjectId` | A reference to the `_id` of the user who owns the document. Indexed for efficient retrieval of a user's documents. |
| `filename` | `String` | The original filename of the uploaded PDF (e.g., "annual_report_2023.pdf"). |
| `storage_path` | `String` | The path to the raw PDF file in the object storage system. |
| `status` | `String` | The current processing state of the document. An enumeration of: `"PENDING"`, `"PROCESSING"`, `"COMPLETED"`, `"FAILED"`. Indexed to allow for querying of documents in a specific state. |
| `page_count` | `Integer` | The total number of pages in the document, determined during processing. |
| `uploaded_at` | `Timestamp` | Timestamp of when the document was uploaded. |

Export to Sheets

### **4.1.3. `conversations` Collection**

This collection stores the history of each chat session, including the messages exchanged and the documents being discussed.

**Table 4.1.3: `conversations` Collection Schema**

| Field Name | Data Type | Description |
| --- | --- | --- |
| `_id` | `ObjectId` | Auto-generated unique identifier and primary key for the conversation. |
| `user_id` | `ObjectId` | A reference to the `_id` of the user who initiated the conversation. Indexed. |
| `title` | `String` | A user-editable or auto-generated title for the chat session (e.g., "Analysis of Q3 Financials"). |
| `document_ids` | `Array` of `ObjectId` | An array of references to the `_id`s in the `documents` collection that are part of this conversation. |
| `created_at` | `Timestamp` | Timestamp of when the conversation was initiated. |
| `messages` | `Array` | An array of embedded documents, representing the full chat history. |
| `messages.message_id` | `ObjectId` | A unique identifier for each individual message within the conversation. |
| `messages.role` | `String` | The role of the message sender. An enumeration of: `"user"` or `"assistant"`. |
| `messages.content` | `String` | The text content of the message. |
| `messages.timestamp` | `Timestamp` | Timestamp of when the message was created. Indexed to allow for sorting messages chronologically. |
| `messages.source_chunks` | `Array` of `String` | For assistant messages only. An array of the unique IDs of the chunks from the Qdrant database that were used as context to generate this response. This enables traceability. |

Export to Sheets

### **4.2. Vector Database (Qdrant) Collection Schema**

The Qdrant vector database will contain a single collection to store all document chunks from all users. Data is logically partitioned and secured using metadata filtering.

### **4.2.1. `document_chunks` Collection**

This collection is the core of the RAG system's retrieval capabilities. Each entry, or "point," represents a single chunk of text from a document.

**Table 4.2.1: `document_chunks` Vector Collection Schema**

| Component | Type / Format | Description |
| --- | --- | --- |
| **Vector** | `Array` of `Float` | A high-dimensional vector representing the semantic meaning of the text chunk. The dimension will match the chosen embedding model (e.g., 1536 for `text-embedding-3-small`). |
| **ID** | `UUID` | A unique, auto-generated identifier for each point (chunk). This ID is referenced in the `conversations.messages.source_chunks` array in MongoDB. |
| **Payload** | `Object` / `Dictionary` | A JSON object containing the metadata associated with the vector. This payload is critical for filtering and for reconstructing context for the LLM. |
| `Payload.document_id` | `String` | The `ObjectId` of the source document from the MongoDB `documents` collection. This field will be indexed in Qdrant for fast filtering. |
| `Payload.user_id` | `String` | The `ObjectId` of the user who owns the document. This field will also be indexed and is essential for enforcing data isolation and security, ensuring users can only query their own documents. |
| `Payload.text` | `String` | The raw text content of the chunk itself. This is returned during retrieval and used to construct the LLM prompt. |
| `Payload.page_number` | `Integer` | The page number in the original PDF where this chunk begins. Used for generating accurate citations. |
| `Payload.chunk_index` | `Integer` | The sequential index of the chunk within the document (e.g., 0, 1, 2...). Useful for debugging and potential future features like retrieving surrounding chunks. |

Export to Sheets

This hybrid schema design ensures that each database is used for what it does best: MongoDB for flexible, transactional metadata management, and Qdrant for high-speed, scalable vector similarity search.

---

## **Section 5: Secure User API Key Management**

The security of user-provided API keys is paramount. A compromise of these keys could lead to unauthorized use of a user's LLM accounts and significant financial loss. This section details a robust, security-first strategy for storing and handling these sensitive credentials.

### **5.1. Architectural Decision: Symmetric Encryption in the Database**

The application requires the ability to use the API keys to make requests to external services on the user's behalf. This fundamental requirement dictates the choice of cryptographic strategy.

- **Rationale for Encryption over Hashing:** One-way hashing (e.g., with bcrypt or SHA-256) is irreversible. While it is the correct approach for storing user passwords (where you only need to verify a match), it is not suitable for API keys that the system must decrypt and use in their plaintext form. Therefore, a reversible method—
    
    **symmetric encryption**—is the appropriate solution. The API keys will be encrypted before being stored in the database and decrypted only in memory, just-in-time for use.
    
- **Database-Level Encryption vs. Dedicated Secrets Manager:** The gold standard for secrets management in large enterprises is a dedicated secrets manager like HashiCorp Vault  or AWS Secrets Manager. These systems provide centralized management, fine-grained access control, and detailed audit logs. However, integrating a dedicated secrets manager introduces significant architectural complexity and operational overhead, including managing access policies and another piece of infrastructure.
    
    For the V1 scope of Cogni-Query, a highly secure implementation of **database-level encryption** provides a more proportionate and pragmatic solution. This approach involves encrypting the sensitive data within the application before it is written to the database. The master key used for this encryption is managed entirely outside the database, typically as a secure environment variable. This strategy effectively protects the keys in the event of a database breach, as the attacker would only gain access to useless ciphertext without the master key. This provides a strong security posture while avoiding premature architectural complexity.
    

### **5.2. Implementation Guide: Encrypting API Keys with Python**

The implementation will leverage a well-vetted, industry-standard cryptographic library to ensure the encryption is secure and correctly implemented.

### **5.2.1. Library Selection**

The system will use the **`cryptography`** Python library, specifically its high-level **`Fernet`** recipe.

`Fernet` provides authenticated symmetric encryption, which guarantees that an encrypted message cannot be modified or read without the key. It uses AES-128 in CBC mode with PKCS7 padding for encryption and HMAC with SHA-256 for authentication, which are strong, standard algorithms.

### **5.2.2. Master Encryption Key Management**

The security of the entire system hinges on the protection of the master encryption key.

1. **Generation:** A single, strong, 32-byte encryption key will be generated using `Fernet.generate_key()`.
2. **Storage and Access:**
    - **Crucially, this `MASTER_ENCRYPTION_KEY` will NEVER be hardcoded in the source code or committed to the Git repository.**
    - **For Local Development:** The key will be stored in a `.env` file at the root of the project. This file will be explicitly listed in `.gitignore` to prevent it from being committed. The application will use the `python-dotenv` library to load this key into the application's environment at runtime.
    - **For Production Deployment:** The `.env` file will not be used in production. Instead, the `MASTER_ENCRYPTION_KEY` will be injected into the container's environment using the deployment platform's native secrets management capabilities (e.g., Docker Secrets, Kubernetes Secrets, or environment variables set in the cloud provider's console).

### **5.2.3. Encryption and Decryption Workflow**

A dedicated security module (e.g., `backend/services/security.py`) will encapsulate all cryptographic operations.

- **Encryption on Write:**
    1. When a user submits an API key through the frontend, the request is sent over HTTPS to the API Gateway.
    2. The API Gateway receives the plaintext key.
    3. It initializes a `Fernet` object with the `MASTER_ENCRYPTION_KEY` loaded from the environment.
    4. It calls `fernet.encrypt(plaintext_key.encode())` to get the encrypted ciphertext.
    5. This binary ciphertext is then stored in the `users.api_keys.encrypted_key` field in the MongoDB database. The plaintext key is immediately discarded from memory.
- **Decryption on Read:**
    1. When the Chat Service needs to make a call to an LLM API, it first retrieves the user's `encrypted_key` from the database.
    2. It initializes a `Fernet` object with the same `MASTER_ENCRYPTION_KEY`.
    3. It calls `fernet.decrypt(encrypted_key).decode()` to retrieve the plaintext key in a local variable.
    4. The plaintext key is used immediately to make the external API request.
    5. As soon as the request is complete, the function scope ends, and the local variable holding the plaintext key is garbage collected. The plaintext key is never logged, written to disk, or returned in any API response.

### **5.3. Security Best Practices and Hardening Checklist**

In addition to the core encryption strategy, the following best practices will be implemented across the application to create a defense-in-depth security posture.

- **Prevent Secret Exposure:** The `.gitignore` file will be configured from the project's inception to ignore `.env` files, `config.py` files, and any other potential secret-containing files.
- **Transport Layer Security (TLS):** All communication between the user's browser and the API Gateway, as well as communication between internal microservices, will be encrypted using HTTPS/TLS to prevent man-in-the-middle attacks.
- **Principle of Least Privilege:** The database user credentials configured for the application will have the minimum set of permissions required to function (e.g., only CRUD operations on its own collections), not administrative privileges.
- **Input Validation and Sanitization:** All user-provided input, including uploaded files, chat messages, and API keys, will be rigorously validated and sanitized on the backend to prevent common vulnerabilities like injection attacks and Cross-Site Scripting (XSS).
- **Dependency Scanning:** Automated tools will be used to scan application dependencies (both Python and JavaScript) for known vulnerabilities.
- **Key Rotation Policy:** While not automated in V1, the operational runbook for the application will include a documented procedure for rotating the `MASTER_ENCRYPTION_KEY` periodically. This involves decrypting all keys with the old master key, re-encrypting them with a new master key, and updating the environment variable in the production deployment.

---

## **Section 6: Project Implementation and Deployment Plan**

This section provides actionable instructions for setting up the development environment, containerizing the application services, and orchestrating the entire stack for both local development and production deployment.

### **6.1. Local Development Environment Setup**

A consistent and easy-to-replicate local development environment is crucial for developer productivity. The setup will rely on standard, widely-used tools.

### **6.1.1. Prerequisites**

Developers will need the following software installed on their local machines:

- Git
- Python 3.11 or newer
- Node.js (LTS version)
- Docker
- Docker Compose

### **6.1.2. Repository Structure**

The project will be organized into a monorepo with a clear directory structure to separate concerns:

`cogni-query/
├──.git/
├──.gitignore
├── docker-compose.yml
├──.env.example
├──.env
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├──.venv/
│   └── app/
│       ├── __init__.py
│       ├── main.py         # API Gateway (FastAPI)
│       ├── chat.py         # Chat Service (FastAPI)
│       ├── worker.py       # Celery app definition
│       ├── tasks.py        # Celery tasks for ingestion
│       ├── models.py       # Pydantic models
│       └── services/
│           ├── security.py # Encryption/Decryption logic
│           └── rag.py      # RAG pipeline logic
└── frontend/
    ├── Dockerfile
    ├── package.json
    ├── next.config.js
    └── src/
        ├── app/
        ├── components/
        └── styles/`

### **6.1.3. Python Backend Setup**

1. Navigate to the `backend/` directory.
2. Create a Python virtual environment: `python3 -m venv.venv`
3. Activate the virtual environment: `source.venv/bin/activate`
4. Install all required dependencies from the `requirements.txt` file: `pip install -r requirements.txt`

The `backend/requirements.txt` file will include:

`fastapi
uvicorn[standard]
celery
redis
pymongo
qdrant-client
cryptography
python-dotenv
langchain
langchain-openai
langchain-google-genai
pypdf2
kreuzberg`

### **6.1.4. Frontend Setup**

1. Navigate to the `frontend/` directory.
2. Install all required Node.js dependencies: `npm install`

The `frontend/package.json` will include dependencies such as:

JSON

`{
  "dependencies": {
    "react": "^18",
    "react-dom": "^18",
    "next": "14.2.3",
    "axios": "^1.6.8"
  }
}`

### **6.2. Containerization Strategy**

Containerization with Docker is a core requirement, enabling consistent environments from development to production and simplifying deployment.

### **6.2.1. `Dockerfile` for Backend Services**

A multi-stage `Dockerfile` will be created in the `backend/` directory. This approach creates a lean, optimized production image by separating the build environment from the final runtime environment.

- **Build Stage:** Installs dependencies into the virtual environment.
- **Final Stage:** Copies the virtual environment and application code from the build stage into a clean, minimal base image (e.g., `python:3.11-slim`). This reduces the final image size and attack surface.

### **6.2.2. `Dockerfile` for Frontend Service**

A similar multi-stage `Dockerfile` will be created in the `frontend/` directory for the Next.js application.

- **Dependency Stage:** Installs `npm` dependencies.
- **Build Stage:** Builds the production-ready Next.js application (`npm run build`).
- **Final Stage:** Copies the built application from the build stage into a lightweight Node.js runtime image (e.g., `node:20-alpine`) and sets the command to start the Next.js server.

### **6.2.3. The `docker-compose.yml` Orchestration File**

This file is the master blueprint for running the entire application stack with a single command. It defines all services, their configurations, networks, and data volumes.

The `docker-compose.yml` file will define the following services:

- **`mongodb`:** Uses the official `mongo` image. A named volume (`mongo_data`) will be attached to persist database files.
- **`qdrant`:** Uses the official `qdrant/qdrant` image. A named volume (`qdrant_data`) will be attached for persistent vector storage.
- **`redis`:** Uses the official `redis:alpine` image for the Celery broker and cache.
- **`api-gateway`:** Builds from the `backend/Dockerfile`. It will be configured to run the FastAPI application using `uvicorn`. It will depend on `mongodb`, `qdrant`, and `redis` to ensure they start first.
- **`chat-service`:** Builds from the same `backend/Dockerfile` but runs a different command to start the chat service application.
- **`celery-worker`:** Builds from the `backend/Dockerfile` and runs the Celery worker command (`celery -A app.worker worker --loglevel=info`). It will be configured to scale horizontally (e.g., `deploy: replicas: 2`).
- **`frontend`:** Builds from the `frontend/Dockerfile` and maps port 3000 to the host, making the UI accessible at `http://localhost:3000`.

**Key Features of the Compose File:**

- **Networking:** All services will be connected to a custom bridge network (`cogni-query-net`), allowing them to communicate with each other using their service names as hostnames (e.g., `mongodb://mongodb:27017`).
- **Environment Variables:** The compose file will use the `env_file` directive to load configuration from the `.env` file at the project root. This is how the `MASTER_ENCRYPTION_KEY` and database credentials will be supplied to the application services.
- **Health Checks and Dependencies:** `depends_on` clauses with health checks will be used to control the startup order. For example, the `api-gateway` will wait until the `mongodb` and `qdrant` services report a healthy status before starting, fulfilling the requirement to handle database setup automatically.

---

## **Section 7: Final `prd.txt` for Automated Build**

This final section synthesizes all preceding design and architectural decisions into a single, comprehensive, machine-readable instruction set. It is intended to be used by a "task-master AI" or a similar automated build system to construct the Cogni-Query application from scratch.

# PROJECT: Cogni-Query

# VERSION: 1.0.0

# DESCRIPTION: A comprehensive product requirements document and technical specification for building the Cogni-Query platform. This document contains all necessary instructions for an automated build system.

## SECTION 1: ENVIRONMENT_SETUP

# This section defines the initial project structure and configuration files.

# 1.1: Create the project directory structure.

CREATE_DIRECTORIES:

- cogni-query/backend/app/services
- cogni-query/frontend/src/app
- cogni-query/frontend/src/components
- cogni-query/frontend/src/styles

# 1.2: Initialize a Git repository in the root directory.

RUN_COMMAND:

- cd cogni-query
- git init

# 1.3: Create the.gitignore file to prevent secrets and unnecessary files from being committed.

CREATE_FILE: cogni-query/.gitignore
FILE_CONTENT:

# Python

**pycache**/
*.pyc
.venv/
*.egg-info/

# Node.js

node_modules/
.next/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Secrets

.env
*.key

# IDE / OS

.idea/
.vscode/
.DS_Store

# 1.4: Create an example environment file for developers.

CREATE_FILE: cogni-query/.env.example
FILE_CONTENT:

# Generate a key using: python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"

MASTER_ENCRYPTION_KEY=

# MongoDB Configuration

MONGO_INITDB_ROOT_USERNAME=root
MONGO_INITDB_ROOT_PASSWORD=example
MONGO_URI=mongodb://root:example@mongodb:27017/

# Redis Configuration

REDIS_URL=redis://redis:6379/0

# LLM API Keys (to be provided by the user in the app)

# OPENAI_API_KEY=

# GEMINI_API_KEY=

# 1.5: Instruct developer to create their local.env file.

PROMPT_USER: "Copy.env.example to.env and fill in the MASTER_ENCRYPTION_KEY."

## SECTION 2: BACKEND_SETUP (Python/FastAPI/Celery)

# This section defines all files and dependencies for the backend services.

# 2.1: Create the Python dependencies file.

CREATE_FILE: cogni-query/backend/requirements.txt
FILE_CONTENT:
fastapi==0.111.0
uvicorn[standard]==0.29.0
celery==5.4.0
redis==5.0.4
pymongo==4.7.2
qdrant-client==1.9.0
cryptography==42.0.7
python-dotenv==1.0.1
langchain==0.2.0
langchain-openai==0.1.7
langchain-google-genai==1.0.5
pypdf2==3.0.1
kreuzberg==0.1.3

# Kreuzberg requires Tesseract and Pandoc to be installed in the Docker image.

# 2.2: Create the main API Gateway application file.

CREATE_FILE: cogni-query/backend/app/main.py
FILE_CONTENT:
"""
Main FastAPI application for the API Gateway.
Handles user authentication, document upload, and routing.
"""
from fastapi import FastAPI, UploadFile, File, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pymongo
from. import models, worker
from.services import security
import os

app = FastAPI(title="Cogni-Query API Gateway")

# Configure CORS

app.add_middleware(
CORSMiddleware,
allow_origins=["http://localhost:3000"],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)

# Database connection

mongo_client = pymongo.MongoClient(os.getenv("MONGO_URI"))
db = mongo_client.cogni_query

@app.post("/api/users/register")
def register_user(user: models.UserCreate):
# Hashing logic for password
hashed_password = security.hash_password(user.password)
# Create user in DB
#... implementation...
return {"message": "User registered successfully"}

@app.post("/api/upload")
def upload_documents(files: list[UploadFile] = File(...)):
# For V1, assume a single user_id for simplicity
user_id = "mock_user_123"
doc_ids =
for file in files:
# 1. Save file to a storage location (e.g., local volume)
file_path = f"/storage/{file.filename}"
with open(file_path, "wb") as buffer:
buffer.write(file.file.read())

      `# 2. Create document record in MongoDB
      doc_data = {
          "user_id": user_id,
          "filename": file.filename,
          "storage_path": file_path,
          "status": "PENDING",
          "page_count": 0,
          "uploaded_at": models.utcnow()
      }
      result = db.documents.insert_one(doc_data)
      doc_id = str(result.inserted_id)
      doc_ids.append(doc_id)
      
      # 3. Dispatch Celery task
      worker.process_document_task.delay(doc_id)
      
  return {"message": "Files uploaded and processing started.", "document_ids": doc_ids}`

# Add other endpoints for login, getting conversations, etc.

#...

# 2.3: Create the Chat Service application file.

CREATE_FILE: cogni-query/backend/app/chat.py
FILE_CONTENT:
"""
FastAPI application for the real-time Chat Service.
Handles the RAG pipeline for user queries.
"""
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from. import models
from.services import rag
import os

app = FastAPI(title="Cogni-Query Chat Service")

@app.post("/api/chat/stream")
async def chat_stream(request: models.ChatRequest):
# Assume user provides API key for now. In reality, retrieve and decrypt from DB.
llm_provider = request.llm_provider
api_key = os.getenv(f"{llm_provider.upper()}_API_KEY")

  `async def stream_generator():
      async for chunk in rag.get_rag_response_stream(request.query, request.conversation_id, llm_provider, api_key):
          yield chunk
          
  return StreamingResponse(stream_generator(), media_type="text/event-stream")`

# 2.4: Create the Celery worker definition.

CREATE_FILE: cogni-query/backend/app/worker.py
FILE_CONTENT:
from celery import Celery
import os

celery_app = Celery(
"tasks",
broker=os.getenv("REDIS_URL"),
backend=os.getenv("REDIS_URL")
)

celery_app.conf.update(
task_serializer="json",
result_serializer="json",
accept_content=["json"]
)

# Import tasks

from. import tasks

process_document_task = celery_app.register_task(tasks.process_document)

# 2.5: Create the Celery tasks file for the ingestion pipeline.

CREATE_FILE: cogni-query/backend/app/tasks.py
FILE_CONTENT:
from.worker import celery_app
from.services import rag
import pymongo
import os

mongo_client = pymongo.MongoClient(os.getenv("MONGO_URI"))
db = mongo_client.cogni_query

@celery_app.task(name="process_document")
def process_document(document_id: str):
db.documents.update_one({"_id": pymongo.ObjectId(document_id)}, {"$set": {"status": "PROCESSING"}})
try:
# 1. Extract text
doc = db.documents.find_one({"_id": pymongo.ObjectId(document_id)})
text, page_count = rag.extract_text_from_pdf(doc['storage_path'])

      `# 2. Chunk text
      chunks = rag.chunk_text(text)
      
      # 3. Embed and index chunks
      rag.embed_and_index_chunks(chunks, document_id, doc['user_id'])
      
      db.documents.update_one(
          {"_id": pymongo.ObjectId(document_id)},
          {"$set": {"status": "COMPLETED", "page_count": page_count}}
      )
  except Exception as e:
      db.documents.update_one(
          {"_id": pymongo.ObjectId(document_id)},
          {"$set": {"status": "FAILED", "error": str(e)}}
      )`

# 2.6: Create the Pydantic models file.

CREATE_FILE: cogni-query/backend/app/models.py
FILE_CONTENT:
from pydantic import BaseModel, Field
from datetime import datetime, timezone

def utcnow():
return datetime.now(timezone.utc)

class UserCreate(BaseModel):
email: str
password: str

class ChatRequest(BaseModel):
query: str
conversation_id: str
llm_provider: str # "openai" or "gemini"

# 2.7: Create the security service for encryption.

CREATE_FILE: cogni-query/backend/app/services/security.py
FILE_CONTENT:
from cryptography.fernet import Fernet
import os

# Load the master key from environment variables

MASTER_KEY = os.getenv("MASTER_ENCRYPTION_KEY").encode()
cipher_suite = Fernet(MASTER_KEY)

def encrypt_api_key(plaintext_key: str) -> bytes:
return cipher_suite.encrypt(plaintext_key.encode())

def decrypt_api_key(encrypted_key: bytes) -> str:
return cipher_suite.decrypt(encrypted_key).decode()

def hash_password(password: str) -> str:
# Use a proper password hashing library like passlib
# For simplicity, this is a placeholder
return f"hashed_{password}"

# 2.8: Create the RAG pipeline service.

CREATE_FILE: cogni-query/backend/app/services/rag.py
FILE_CONTENT:

# This file will contain the detailed logic for:

# extract_text_from_pdf (using Kreuzberg)

# chunk_text (using RecursiveCharacterTextSplitter from LangChain)

# embed_and_index_chunks (using Qdrant client and OpenAI/Gemini client)

# get_rag_response_stream (querying Qdrant, building the prompt, and calling the LLM)

# This is a placeholder for the full implementation logic.

pass

## SECTION 3: FRONTEND_SETUP (React/Next.js)

# This section defines the key frontend components.

# 3.1: Initialize the Next.js application.

RUN_COMMAND:

- cd cogni-query
- npx create-next-app@latest frontend --ts --tailwind --eslint --app --src-dir --import-alias "@/*"

# 3.2: Create the main Chat component.

CREATE_FILE: cogni-query/frontend/src/components/ChatWindow.jsx
FILE_CONTENT:
// React component for the chat interface.
// Will manage state for messages, user input, and API calls.
// Will render the conversation history and handle streaming responses.
// This is a placeholder for the full React component code.
import React, { useState, useEffect } from 'react';

export default function ChatWindow() {
const [messages, setMessages] = useState();
const [input, setInput] = useState('');

`const handleSend = async () => {
  // Logic to send input to backend and handle streaming response
};

return (
  <div>
    <div className="message-list">
      {/* Map over messages and render them */}
    </div>
    <input value={input} onChange={(e) => setInput(e.target.value)} />
    <button onClick={handleSend}>Send</button>
  </div>
);`

}

## SECTION 4: DOCKER_CONFIGURATION

# This section defines the Dockerfiles and the Docker Compose file for orchestration.

# 4.1: Create the Dockerfile for the backend.

CREATE_FILE: cogni-query/backend/Dockerfile
FILE_CONTENT:

# Stage 1: Build stage

FROM python:3.11-slim as builder

WORKDIR /app

# Install system dependencies for Kreuzberg

RUN apt-get update && apt-get install -y tesseract-ocr pandoc

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt.
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Final stage

FROM python:3.11-slim

WORKDIR /app

# Install system dependencies again for the final image

RUN apt-get update && apt-get install -y tesseract-ocr pandoc

COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY./app /app/app

# Command to run will be specified in docker-compose.yml

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# 4.2: Create the Dockerfile for the frontend.

CREATE_FILE: cogni-query/frontend/Dockerfile
FILE_CONTENT:

# Stage 1: Dependencies

FROM node:20-alpine AS deps
WORKDIR /app
COPY package*.json./
RUN npm install

# Stage 2: Builder

FROM node:20-alpine AS builder
WORKDIR /app
COPY --from=deps /app/node_modules./node_modules
COPY..
RUN npm run build

# Stage 3: Runner

FROM node:20-alpine AS runner
WORKDIR /app

ENV NODE_ENV=production

COPY --from=builder /app/public./public
COPY --from=builder /app/.next./.next
COPY --from=builder /app/node_modules./node_modules
COPY --from=builder /app/package.json./package.json

EXPOSE 3000
CMD ["npm", "start"]

# 4.3: Create the Docker Compose file.

CREATE_FILE: cogni-query/docker-compose.yml
FILE_CONTENT:
version: '3.8'

services:
mongodb:
image: mongo:6.0
container_name: mongodb
ports:
- "27017:27017"
volumes:
- mongo_data:/data/db
environment:
- MONGO_INITDB_ROOT_USERNAME=MONGOINITDBROOTUSERNAME−MONGOINITDBROOTPASSWORD={MONGO_INITDB_ROOT_PASSWORD}
networks:
- cogni-query-net
healthcheck:
test:
interval: 10s
timeout: 5s
retries: 5

`qdrant:
  image: qdrant/qdrant:v1.9.0
  container_name: qdrant
  ports:
    - "6333:6333"
    - "6334:6334"
  volumes:
    - qdrant_data:/qdrant/storage
  networks:
    - cogni-query-net
  healthcheck:
    test:
    interval: 10s
    timeout: 5s
    retries: 5

redis:
  image: redis:7-alpine
  container_name: redis
  networks:
    - cogni-query-net
  healthcheck:
    test:
    interval: 10s
    timeout: 5s
    retries: 5

api-gateway:
  build:
    context:./backend
    dockerfile: Dockerfile
  container_name: api-gateway
  command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
  ports:
    - "8000:8000"
  volumes:
    -./backend/app:/app/app
    - storage_data:/storage
  env_file:
    -./.env
  networks:
    - cogni-query-net
  depends_on:
    mongodb:
      condition: service_healthy
    qdrant:
      condition: service_healthy
    redis:
      condition: service_healthy

celery-worker:
  build:
    context:./backend
    dockerfile: Dockerfile
  container_name: celery-worker
  command: celery -A app.worker worker --loglevel=info -Q default -c 2
  volumes:
    -./backend/app:/app/app
    - storage_data:/storage
  env_file:
    -./.env
  networks:
    - cogni-query-net
  depends_on:
    mongodb:
      condition: service_healthy
    qdrant:
      condition: service_healthy
    redis:
      condition: service_healthy

frontend:
  build:
    context:./frontend
    dockerfile: Dockerfile
  container_name: frontend
  ports:
    - "3000:3000"
  networks:
    - cogni-query-net
  depends_on:
    - api-gateway`

volumes:
mongo_data:
qdrant_data:
storage_data:

networks:
cogni-query-net:
driver: bridge

## SECTION 5: EXECUTE_BUILD

# This section contains the final command to build and run the entire application stack.

RUN_COMMAND:

- cd cogni-query
- docker-compose up --build -d

# END_OF_DOCUMENT
