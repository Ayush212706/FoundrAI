from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

print("Loading PDFs...")

loader = DirectoryLoader(
    "knowledge",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

documents = loader.load()

print(f"Loaded {len(documents)} pages.")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = splitter.split_documents(documents)

print(f"Created {len(docs)} chunks.")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.from_documents(
    docs,
    embeddings
)

db.save_local("vector_db")

print("✅ Vector database created successfully!")