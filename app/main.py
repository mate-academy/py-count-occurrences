def count_occurrences(phrase: str, letter: str) -> int:
    """
    It takes a phrase and a letter and calculates the number of times
    the letter appears in the phrase. The function is case-insensitive.

    """
    return phrase.lower().count(letter.lower())
