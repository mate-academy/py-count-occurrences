def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count occurrences of a letter or substring in a phrase (case insensitive).

    Args:
        phrase (str): The text in which to search.
        letter (str): The letter or substring to count. Empty stieng return 0.

    Returns:
        int: Number of times 'letter' appears in 'phrase' (case-insensitive).
    """
    if letter == "":
        return 0

    return phrase.lower().count(letter.lower())
