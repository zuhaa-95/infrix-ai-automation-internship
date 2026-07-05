from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_training_data():
    with open('training_data.txt', 'r') as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def get_relevant_docs(query, top_n=3):
    docs = load_training_data()
    vectorizer = TfidfVectorizer()
    all_texts = [query] + docs
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    top_indices = similarities.argsort()[-top_n:][::-1]
    return [docs[i] for i in top_indices]