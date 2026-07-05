# Week 03 - Crime Scene Investigator Bot

An AI-powered crime scene investigation chatbot that combines Natural Language Processing (NLP) techniques with Large Language Models (LLMs) through the Groq Inference API.

The system processes user descriptions of crime scenes through a full NLP pipeline — text preprocessing, intent detection, named entity recognition, and TF-IDF based document retrieval — before generating intelligent investigation reports.

## Project Structure

Week-03/
│
├── README.md
│
├── app.py
├── requirements.txt
├── training_data.txt
│
├── llm/
│   ├── generator.py
│   ├── model.py
│   └── prompt_builder.py
│
└── nlp/
    ├── preprocess.py
    ├── tfidf.py
    ├── intent.py
    ├── ner.py
    └── pipeline.py

## Features

- Text preprocessing and cleaning
- TF-IDF based document retrieval
- Intent classification (SUSPECT, EVIDENCE, MOTIVE, TIME_OF_DEATH, GENERAL)
- Named Entity Recognition for weapons, locations and names
- Prompt engineering and context-aware prompt construction
- Integration with Groq LLM API
- Streamlit-based detective themed chat interface
- Modular architecture for easy extension

## Workflow

User Query
    │
    ▼
Text Preprocessing
    │
    ▼
Intent Detection
    │
    ▼
Named Entity Recognition
    │
    ▼
TF-IDF Document Retrieval
    │
    ▼
Prompt Builder
    │
    ▼
Groq LLM API
    │
    ▼
Investigation Report

## Technologies Used

- Python 3.x
- Streamlit
- Scikit-learn
- Groq Inference API
- NLP Techniques
  - Tokenization
  - Text Cleaning
  - TF-IDF Vectorization
  - Intent Classification
  - Named Entity Recognition

## Installation

1. Clone the Repository

git clone https://github.com/zuhaa-95/infrix-ai-automation-internship.git
cd infrix-ai-automation-internship/Week-03

2. Install Dependencies

pip install -r requirements.txt

3. Configure Groq API Token

Add your Groq API key in llm/model.py:
GROQ_API_KEY = "your_groq_api_key_here"

4. Run the Application

streamlit run app.py

## Example Interaction

User: I found a dead body in the kitchen with a knife nearby and blood on the floor

Bot: Location: Kitchen
     Observed Evidence:
     1. Blood: The presence of blood suggests a violent incident...
     2. Dead Body: The presence indicates a potential homicide...
     3. Physical Evidence: A thorough search will be conducted...

## Learning Objectives

- NLP fundamentals and pipeline design
- Intent classification techniques
- Named Entity Recognition
- TF-IDF based document retrieval
- Prompt engineering for LLMs
- Groq LLM API integration
- Building AI powered chat applications
- Modular Python project structure

## Author

Zuhaa Hayat
Training Program - Week 03
Building practical AI solutions with NLP and Large Language Models.
