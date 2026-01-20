def count_occurrences(phrase: str, letter: str) -> int:
    phrase_lower = phrase.lower()
    count_occurrences = phrase_lower.count(letter.lower())
    return count_occurrences
    pass
