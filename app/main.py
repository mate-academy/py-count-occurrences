def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count the number of occurrences of a character in a string (case-insensitive).

    Args:
        phrase (str): The string in which to search.
        letter (str): The character to count.

    Returns:
        int: The number of times the character appears in the string.
    """
    if not letter:
        return 0

    return phrase.lower().count(letter.lower())