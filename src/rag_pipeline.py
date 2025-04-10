from langchain.chains import RetrievalQA
from langchain.llms import OpenAI, HuggingFaceHub
from dotenv import load_dotenv

# Option 1: Load from current directory
load_dotenv()  
def setup_rag_chain(vector_db, llm_model="gpt-3.5-turbo"):
    # Option 1: OpenAI (paid)
    # llm = OpenAI(model_name=llm_model)
    # Option 2: HuggingFace (free)
    
    llm = HuggingFaceHub(repo_id="mistralai/Mistral-7B-Instruct-v0.1")
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_db.as_retriever(search_kwargs={"k": 1}),
        return_source_documents=True,  # Critical: hides sources
        verbose=False  # Disables LangChain's internal logging
    )
    return qa_chain 