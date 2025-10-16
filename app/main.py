def count_occurrences(phrase: str, letter: str) -> int:
    """
    Counts occurrences of `letter` (or substring) in `phrase`, case-insensitive.

    Parameters:
        phrase: str — the string to search within
        letter: str — the letter (or substring) to count

    Returns:
        int — number of occurrences (case-insensitive)

    Raises:
        ValueError: if `letter` is an empty string

    Example:
        >>> count_occurrences("Hello, world", "l")
        3

    Note:
        Python's str.count('') returns len(phrase) + 1. This function explicitly
        forbids an empty `letter` and raises ValueError to avoid that surprising result.
    """
    if not letter:
        raise ValueError("letter cannot be empty")

    return phrase.lower().count(letter.lower())
