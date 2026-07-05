def build_prompt(query, intent, entities, docs):
    context = "\n".join(docs)
    entity_str = str(entities) if entities else "None"
    
    prompt = f"""You are a Crime Scene Investigator AI assistant.
    
Context from knowledge base:
{context}

User Query: {query}
Detected Intent: {intent}
Extracted Entities: {entity_str}

Analyze the crime scene and provide a detailed investigation response:"""
    
    return prompt