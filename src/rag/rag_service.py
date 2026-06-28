from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(
    "vector_db",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = db.as_retriever(search_kwargs={"k": 3})

llm = ChatOllama(
    model="gemma3:4b",
    temperature=0.7
)


def ask_rag(question):
    docs = retriever.invoke(question)

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
You are FoundrAI, an AI Startup Mentor.

Use the retrieved context as your primary source.

If the answer is not completely available in the context,
say so clearly, then provide general startup knowledge
while mentioning that the additional information is based
on your general knowledge.

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    return response.content