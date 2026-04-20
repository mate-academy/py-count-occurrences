def count_occurrences(phrase: str, letter: str) -> int:
    # приводимо до одного регістру
    phrase_lower = phrase.lower()
    letter_lower = letter.lower()
    
    # підрахунок входжень
    return phrase_lower.count(letter_lower)
