def count_occurrences(phrase: str, letter: str) -> int:
    """
    Counts the number of times a given letter appears in a phrase, case-insensitively.

    Parameters:
        phrase (str): The string to search within.
        letter (str): The letter to count occurrences of.

    Returns:
        int: The number of times the letter appears in the phrase.
    """

    return phrase.lower().count(letter.lower())
