def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count occurrences of a letter in a phrase (case insensitive).
    :param phrase: The phrase to search within.
    :type phrase: str
    :param letter: The letter to count occurrences of. Should be a single character.
    :type letter: str
    :return: Number of occurrences of the letter in the phrase.
    :rtype: int
    """
    return phrase.lower().count(letter.lower())