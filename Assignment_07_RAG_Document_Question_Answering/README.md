# Assignment 07 – Retrieval-Augmented Generation (RAG) Document Question Answering

## Overview

This project was completed as part of the **Celebal Excellence Internship (CEI) 2026** under the **Data Science (DS001)** track at **Celebal Technologies**.

The objective of this project was to develop a Retrieval-Augmented Generation (RAG) system capable of answering user questions based on custom documents. Unlike traditional language models, the system retrieves relevant document chunks before generating responses, improving factual accuracy and enabling question answering over domain-specific knowledge.

---

## Problem Statement

**Develop a Retrieval-Augmented Generation (RAG) based Document Question Answering System.**

The project involved designing an end-to-end pipeline covering:

- Document Loading
- PDF Processing
- Text Chunking
- Embedding Generation
- Vector Database Creation
- Similarity Search
- Context Retrieval
- Retrieval-Augmented Generation (RAG)
- Question Answering over Custom Documents

---

## Dataset

Instead of using a public dataset, this project uses a custom PDF document:

**Water Pollution – Sources and Causes.pdf**

The document contains educational content on:

- Water Pollution
- Sources of Water Pollution
- Point and Non-Point Sources
- Causes of Water Pollution
- Environmental Impacts

The RAG pipeline indexes this document and answers natural language questions using its contents.

---

## RAG Pipeline

The system consists of the following stages:

1. Document Loading
2. Text Extraction
3. Text Chunking
4. Embedding Creation
5. Vector Store Construction
6. Semantic Similarity Search
7. Context Retrieval
8. Answer Generation using a Large Language Model (LLM)

---

## Files

| File | Description |
|------|-------------|
| RAG_Document_QA.ipynb | Completed RAG Document Question Answering Project |
| Water Pollution_Sources and Causes.pdf | Custom knowledge base used by the RAG pipeline |
| requirements.txt | Python dependencies |
| README.md | Project documentation |

---

## Tools & Libraries Used

- Python
- LangChain
- FAISS
- Hugging Face Transformers
- Sentence Transformers
- PyPDF
- Google Generative AI / Gemini
- NumPy
- Google Colab / Jupyter Notebook

---

## Learning Outcomes

Through this project, the following concepts were practiced:

- Retrieval-Augmented Generation (RAG)
- Document Question Answering
- Prompt Engineering
- Vector Databases
- Embeddings
- Semantic Search
- Text Chunking
- Similarity Search
- Context Retrieval
- LangChain
- FAISS
- Large Language Models (LLMs)

---

## Key Observations

- Retrieval significantly improves factual grounding by supplying relevant document context.
- Semantic embeddings enable efficient similarity search across document chunks.
- RAG systems are well suited for answering questions over private or domain-specific documents.
- The quality of chunking and embedding models directly impacts retrieval accuracy.

---

## Author

**Subrata Kumar Dey**

Data Science Intern – CEI 2026

B.Tech CSE (Cyber Security & Privacy)

DIT University
