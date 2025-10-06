def count_occurrences(phrase: str, letter: str) -> int:
    """Return how many times `letter` appears in `phrase` (case-insensitive).

    Parameters:
    - phrase: str — the string to search in
    - letter: str — the letter to count

    Returns:
    - int: number of occurrences of `letter` in `phrase` (case-insensitive)

    Examples:
    - count_occurrences("letter", "t") -> 2
    - count_occurrences("ABC", "a") -> 1
    """
    return phrase.lower().count(letter.lower())
