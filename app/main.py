def count_occurrences(phrase: str, letter: str) -> int:
    """Counts how many times a given letter appears in a phrase, ignoring case.
    Parameters:
        phrase (str): The string to search in.
        letter (str): The letter or substring to count.
    Returns:
        int: The number of times the letter appears in the phrase.
    Notes:
        Counting is case-insensitive.
    Examples:
        count_occurrences("letter", "t") -> 2
        count_occurrences("ABC", "a") -> 1
    """
    return phrase.lower().count(letter.lower())
