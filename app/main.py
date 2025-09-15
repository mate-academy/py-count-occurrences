def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count the number of occurrences of `letter` in `phrase`.
    The function is case insensitive.
    :param phrase: str - to search
    :param letter: str - to count
    :returns: int - number of times `letter` occurs in `phrase`
    """
    return phrase.lower().count(letter.lower())
