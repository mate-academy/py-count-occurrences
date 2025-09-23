def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count how many times a letter appears in a phrase.

    Args:
        phrase (str): The phrase to search.
        letter (str): The target letter.

    Returns:
        int: The number of times the letter appears in the phrase.
    """
    return phrase.lower().count(letter.lower())
