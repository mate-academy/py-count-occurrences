def count_occurrences(phrase: str, letter: str) -> int:
    phrase_lower = phrase.lower()
    counted = phrase_lower.count(letter.lower())
    return counted
    pass
