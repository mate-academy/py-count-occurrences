def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count how many times a letter appears in a phrase (case-insensitive).

    Args:
        phrase (str): The text where to search.
        letter (str): The character to count.

    Returns:
        int: Number of times the letter appears.
    """
    if not letter:
        return 0

    return phrase.lower().count(letter.lower())
