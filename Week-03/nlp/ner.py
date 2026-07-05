import re

def extract_entities(text):
    entities = {}
    
    # Extract names (capitalized words)
    names = re.findall(r'\b[A-Z][a-z]+\b', text)
    if names:
        entities['names'] = names
    
    # Extract locations
    locations = ['room', 'kitchen', 'bedroom', 'office', 'street', 'house', 'building']
    found_locations = [loc for loc in locations if loc in text.lower()]
    if found_locations:
        entities['locations'] = found_locations
    
    # Extract weapons
    weapons = ['gun', 'knife', 'poison', 'rope', 'bat', 'hammer', 'pistol']
    found_weapons = [w for w in weapons if w in text.lower()]
    if found_weapons:
        entities['weapons'] = found_weapons
    
    return entities