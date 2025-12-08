def count_occurrences(phrase: str, letter: str) -> int:
    """
    Calculates the number of times a specific letter appears in a phrase.

    The count is case-insensitive.

    Parameters
    ----------
    phrase : str
        The text phrase to search within.
    letter : str
        The letter (a single character) to count the occurrences of.

    Returns
    -------
    int
        The total count of the letter in the phrase, ignoring case.

    Examples
    --------
    >>> count_occurrences("Letter", "t")
    2
    >>> count_occurrences("abc", "d")
    0
    >>> count_occurrences("ABC", "a")
    1
    """
    return phrase.lower().count(letter.lower())
