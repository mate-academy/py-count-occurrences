def count_occurrences(phrase: str, letter: str) -> int:
    """
    Counts the number of times a letter appears in a phrase,
case-insensitively.
    Args:
        phrase: The string to search within.
        letter: The letter to count the occurrences of.

    Returns:
        The total number of times the letter appears in the phrase.
    """
    return phrase.lower().count(letter.lower())
