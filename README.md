# RAG Knowledge Assistant 🚀

[![Streamlit Demo](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-demo-link.streamlit.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> A Retrieval-Augmented Generation (RAG) system for enterprise document Q&A.

## Features
- 📂 Upload PDFs and extract text
- 🔍 Semantic search with vector embeddings (ChromaDB)
- 💬 Generate answers using Mistral-7B/GPT-3.5
- 🖥️ Streamlit/FastAPI web interface

## Tech Stack
| Component       | Technology |
|----------------|------------|
| LLM            | Mistral-7B/HuggingFace Hub |
| Vector Store   | ChromaDB   |
| Embeddings     | Sentence Transformers |
| Framework      | LangChain  |

## Quick Start
1. Clone repo:
   ```bash
   git clone https://github.com/yourusername/RAG-Knowledge-Assistant.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run Streamlit app:
   ```bash
   streamlit run src/app.py
   ```

## Demo
![Demo GIF](assets/demo.gif) *(Add a short screen recording)*

## License
MIT © Your Name