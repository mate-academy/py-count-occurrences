def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count the number of times a letter appears in a phrase (case-insensitive).

    Args:
        phrase (str): The string to search in.
        letter (str): The letter to count.

    Returns:
        int: The number of occurrences of the letter.
    """
    if len(letter) != 1:
        raise ValueError("letter must be a single character")
    
    return phrase.lower().count(letter.lower())

