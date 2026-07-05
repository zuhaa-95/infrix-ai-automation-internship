def detect_intent(text):
    text = text.lower()
    
    if any(word in text for word in ['suspect', 'who', 'person', 'killer', 'criminal']):
        return 'SUSPECT'
    elif any(word in text for word in ['evidence', 'clue', 'found', 'weapon', 'fingerprint']):
        return 'EVIDENCE'
    elif any(word in text for word in ['motive', 'why', 'reason']):
        return 'MOTIVE'
    elif any(word in text for word in ['time', 'when', 'death', 'died']):
        return 'TIME_OF_DEATH'
    else:
        return 'GENERAL'