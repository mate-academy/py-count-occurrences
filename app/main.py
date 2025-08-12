def count_occurrences(phrase: str, letter: str) -> int:
    """
    Counts the number of times a given letter appears in a phrase, case-insensitive.

    Args:
        phrase (str): The string to search within.
        letter (str): The letter to count.

    Returns:
        int: The number of occurrences of letter in phrase.
    """
    return phrase.lower().count(letter.lower())

