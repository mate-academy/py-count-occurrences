def count_occurrences(phrase: str, letter: str) -> int:
    """Count the number of occurrences of `letter` in `phrase`.

    Parameters
    ----------
    phrase : str
        The phrase to search within.
    letter : str
        The letter to count in the phrase.

    Returns
    -------
    int
        The number of times `letter` occurs in `phrase`.
    """
    phrase_lower =phrase.lower()
    counter = phrase_lower.count(letter.lower())
    return counter



