def count_occurrences(phrase: str, letter: str) -> int:
    """Count how many times a letter appears in a phrase.

    Matching is case-insensitive. If `letter` is empty, returns 0.
    Only the first character of `letter` is considered.

    Args:
        phrase: The text where the search is performed.
        letter: The letter to count (only the first char is used).

    Returns:
        The number of occurrences of `letter` in `phrase`.
    """
    if not letter:
        return 0
    return phrase.lower().count(letter[0].lower())