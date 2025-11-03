def count_occurrences(phrase: str, letter: str) -> int:
    """
    Returns the number of times `letter` appears in `phrase` (case-insensitive).
    """
    return phrase.lower().count(letter.lower())
