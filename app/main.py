def count_occurrences(phrase: str, letter: str) -> int:

    phrase_lower = phrase.lower()

    return phrase_lower.count(letter.lower())
