# RAG Legal Assistant (in progress)

A Retrieval-Augmented Generation (RAG) pipeline for answering questions about Slovak legislation in plain language
- making legal information accessible to non-native speakers and foreigners in Slovakia.

## Motivation
Understanding legal requirements in a foreign country is challenging. 
This project aims to bridge the gap between complex legal texts 
and everyday users by providing clear, context-aware answers based on official Slovak laws.

## How it works
1. Legal text is scraped and extracted from PDF documents (135 pages)
2. Text is cleaned, chunked and preprocessed
3. Chunks are embedded and stored for retrieval
4. User query triggers relevant chunk retrieval
5. LLM generates an answer based on retrieved context

## Technologies
- Python
- LangChain
- Web scraping (Beautiful Soup)
- PDF extraction
- Text chunking strategies
- Embeddings and vector search
- LLMs

## Current Status
- [x] Data collection and preprocessing
- [x] Initial RAG pipeline
- [x] Text chunking and retrieval logic
- [ ] LLM integration
- [ ] User interface
- [ ] Evaluation framework

## Disclaimer
This tool is for informational purposes only and does not constitute legal advice.

## Code Usage
This repository is for educational and portfolio purposes. For technical evaluation during job interviews, full access can be provided upon request.
