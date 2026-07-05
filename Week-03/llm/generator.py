from llm.prompt_builder import build_prompt
from llm.model import query_model

def generate_answer(query, intent, entities, docs):
    prompt = build_prompt(query, intent, entities, docs)
    return query_model(prompt)