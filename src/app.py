import streamlit as st
from vector_db import create_vector_store
from data_loader import load_and_chunk_documents
from rag_pipeline import setup_rag_chain

st.title("Enterprise Knowledge Assistant 🚀")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    chunks = load_and_chunk_documents(".")
    vector_db = create_vector_store(chunks)
    qa_chain = setup_rag_chain(vector_db)
    
    query = st.text_input("Ask a question:")
    if query:
        response = qa_chain({"query": query})
        st.write("Answer:", response["result"])
        st.write("Sources:", [doc.metadata["source"] for doc in response["source_documents"]])