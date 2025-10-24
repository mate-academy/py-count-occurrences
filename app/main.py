def count_occurrences(phrase: str, letter: str) -> int:
    """
    Counts the number of occurrences of a specified letter
    in a given phrase, ignoring case.

    Parameters:
    phrase (str): The string in which to count occurrences.
    letter (str): The letter to count in the phrase.

    Returns:
    int: The number of times the letter appears in the phrase,
    case-insensitively.
    """
    phrase_lower = phrase.lower()
    counter = phrase_lower.count(letter.lower())
    return counter
