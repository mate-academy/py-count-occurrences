def count_occurrences(phrase: str, letter: str) -> int:
    """
    Counts the number of occurrences of a given letter in a string, ignoring case sensitivity.

    Args:
        phrase (str): The string in which to search.
        letter (str): The letter to count occurrences of.

    Returns:
        int: The number of times the letter appears in the string.
    """
    return phrase.lower().count(letter.lower())