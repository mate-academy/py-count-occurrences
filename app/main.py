def count_occurrences(phrase: str, letter: str) -> int:
    """Count occurrences of letter in phrase case-insensitively.
    Parameters: phrase (str), letter (str)
    Returns: int count
    """
    return phrase.lower().count(letter.lower())
