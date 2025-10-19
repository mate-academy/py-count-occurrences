def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count how many times a letter (or substring) appears in the phrase.

    Args:
        phrase (str): The text where we search.
        letter (str): The letter or part of text we count.

    Returns:
        int: How many times it appears.
    """
    return phrase.lower().count(letter.lower())
