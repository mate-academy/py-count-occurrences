def count_occurrences(phrase: str, letter: str) -> int:
    """
    Counts the number of times a letter appears in a phrase, case-insensitively.
    """
    return phrase.lower().count(letter.lower())