def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count occurrences of a letter in a phrase.

    :param phrase: The phrase to search within.
    :param letter: The letter to count.
    :return: The number of occurrences of the letter.
    """
    return phrase.lower().count(letter.lower())
