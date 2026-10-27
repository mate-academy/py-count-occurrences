def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count occurrences of a letter or substring in a phrase.

    Performs case-insensitive counting of how many times the given letter
    or substring appears in the phrase.

    Args:
        phrase (str): The phrase to search within
        letter (str): The letter or substring to count occurrences of

    Returns:
        int: Number of occurrences of the letter/substring in the phrase

    Note:
        Empty strings as the letter parameter will return 0.
    """
    if letter == "":
        return 0
    return phrase.lower().count(letter.lower())
