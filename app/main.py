def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count how many times a letter appears in a phrase.
    """
    return phrase.lower().count(letter.lower())
