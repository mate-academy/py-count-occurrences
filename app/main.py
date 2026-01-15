def count_occurrences(phrase: str, letter: str) -> int:
    """
    Return the number of times a letter appears in a phrase (case-insensitive).

    Args:
        phrase (str): The string where the search is performed.
        letter (str): The character to count in the phrase.

    Returns:
        int: The number of occurrences of the given letter in the phrase.
    """
    if not isinstance(phrase, str) or not isinstance(letter, str):
        raise TypeError("Both arguments must be strings")
    if len(letter) != 1:
        return 0
    return phrase.lower().count(letter.lower())
