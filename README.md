# Troubleshooting Agent

A simple AI-powered troubleshooting chatbot built with **Python** and **FastAPI**.

This project started as a collection of Coursera practice activities and is gradually being expanded into a more realistic troubleshooting agent. The goal is to explore different approaches to building intelligent support systems, from basic keyword matching to NLP pipelines and, eventually, transformer-based language models.

## Current Features

* FastAPI backend
* Simple chat API
* Knowledge base stored as JSON
* Input validation service
* NLP preprocessing with:

  * NLTK tokenization
  * Part-of-Speech (POS) tagging
  * spaCy Named Entity Recognition (NER)
  * Hugging Face sentiment analysis
* Structured service-based architecture
* Basic application logging

## Project Structure

```text
backend/
├── main.py
├── routers/
├── services/
├── models/
└── troubleshooting_knowledge_base.json

frontend/
├── index.html
├── styles.css
└── chatbot.js
```

## Technologies

* Python
* FastAPI
* NLTK
* spaCy
* Transformers (Hugging Face)
* HTML
* CSS
* JavaScript

## Running the Project

Clone the repository and install the dependencies.

Start the application with:

```bash
uvicorn backend.main:app --reload
```

Then open your browser and navigate to:

```
http://127.0.0.1:8000/
```

## Planned Features

* Interactive chat interface
* Improved troubleshooting workflow
* Expanded knowledge base
* Better validation and logging
* Machine learning issue classification
* DistilBERT-based intent detection
* LLM integration
* Conversation memory
* Automated troubleshooting actions

## Status

Work in progress.