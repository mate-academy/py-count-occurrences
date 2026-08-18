def count_occurrences(phrase: str, letter: str) -> int:
    """Return number of occurrences of `letter` in `phrase` (case-insensitive).
    If `letter` is empty, return 0.
    """
    if not letter:
        return 0
    return phrase.lower().count(letter.lower())
