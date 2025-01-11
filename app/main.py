def count_occurrences(phrase: str, letter: str) -> int:
    phrase_lower = phrase.lower()
    result = phrase_lower.count(letter.lower())

    return result
