def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count the number of occurrences of a letter in a phrase.

    Args:
        phrase (str): The phrase in which to count occurrences.
        letter (str): The letter to count.

    Returns:
        int: The number of occurrences of the letter in the phrase.
    """
    if len(letter) != 1:
        raise ValueError("The 'letter' argument must be a single character.")

    return phrase.lower().count(letter.lower())
