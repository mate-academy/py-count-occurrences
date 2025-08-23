def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count how many times a given letter appears in a phrase (case-insensitive).

    Args:
        phrase (str): The text in which to search.
        letter (str): A single character to count (case-insensitive).

    Returns:
        int: The number of times `letter` occurs in `phrase`.

    Raises:
        ValueError: If `letter` is not a single character.
    """
    if len(letter) != 1:
        raise ValueError("`letter` must be a single character.")

    return phrase.lower().count(letter.lower())