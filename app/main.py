def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count the number of occurrences of a specific letter in a phrase (case-insensitive).

    Args:
        phrase (str): The input phrase to search in
        letter (str): The letter to count occurrences of

    Returns:
        int: The number of times the letter appears in the phrase

    Example:
        >>> count_occurrences("Hello World", "l")
        3
        >>> count_occurrences("Python", "y")
        1
    """
    return phrase.lower().count(letter.lower())
