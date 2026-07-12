def count_occurrences(phrase: str, letter: str) -> int:
    """
    Return the number of times `letter` appears in `phrase`, ignoring case.

    Parameters:
        phrase: The input string in which to search.
        letter: The letter to count.

    Returns:
        The number of occurrences of `letter` in `phrase`.
    """
    phrase = phrase.lower()
    letter = letter.lower()
    return phrase.count(letter)
