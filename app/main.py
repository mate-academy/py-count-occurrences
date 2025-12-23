def count_occurrences(phrase: str, letter: str) -> int:
    """
    Counts the number of times a given letter appears in a phrase, case-insensitively.

    Args:
        phrase (str): The string in which to search for the letter.
        letter (str): The letter to count within the phrase.

    Returns:
        int: The number of occurrences of the letter in the phrase.
    """
    # function body...
    return phrase.lower().count(letter.lower())
