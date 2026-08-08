def count_occurrences(phrase: str, letter: str) -> int:
    """Count the occurrences of a letter in a phrase (case-insensitive).

    Args:
        phrase (str): The input string to search in.
        letter (str): The character to count.

    Returns:
        int: The number of times the letter appears in the phrase.
    """
    return phrase.lower().count(letter.lower())
