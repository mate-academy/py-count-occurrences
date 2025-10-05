def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count how many times a letter appears in a phrase.
    """
    if len(letter) != 1:
        return phrase.lower().count(letter.lower())
