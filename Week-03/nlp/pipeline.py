from nlp.preprocess import preprocess
from nlp.intent import detect_intent
from nlp.ner import extract_entities
from nlp.tfidf import get_relevant_docs

def run_pipeline(query):
    cleaned = preprocess(query)
    intent = detect_intent(query)
    entities = extract_entities(query)
    relevant_docs = get_relevant_docs(cleaned)
    
    return {
        'original_query': query,
        'cleaned_query': cleaned,
        'intent': intent,
        'entities': entities,
        'relevant_docs': relevant_docs
    }