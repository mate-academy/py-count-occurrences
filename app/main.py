def count_occurrences(phrase: str, letter: str) -> int:
    """
    Counts how many times a given letter appears in a phrase, ignoring case.

    Args:
        phrase (str): The input string to search within.
        letter (str): The letter to count in the phrase.

    Returns:
        int: The number of times the letter appears in the phrase.
    """
    return phrase.lower().count(letter.lower())
