def count_occurrences(phrase: str, letter: str) -> int:
    phrase_lower = phrase.lower()
    letter_lower = letter.lower()

    occurrences = phrase_lower.count(letter_lower)
    return occurrences

    pass
