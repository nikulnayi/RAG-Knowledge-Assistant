from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

def create_vector_store(chunks, embedding_model="sentence-transformers/all-mpnet-base-v2"):
    # Option 1: OpenAI (paid, better accuracy)
    # embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    
    # Option 2: HuggingFace (free)
    embeddings = HuggingFaceEmbeddings(model_name=embedding_model)
    
    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="db"
    )
    return vector_db