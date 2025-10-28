def count_occurrences(phrase: str, letter: str) -> int:
    """
    Counts the number of times a letter appears in a phrase,
    ignoring case sensitivity.

    :param phrase: The phrase where the count will be performed.
    :type phrase: str
    :param letter: The letter to be counted in the phrase.
    :type letter: str
    :returns: The number of occurrences of the letter in the phrase.
    :rtype: int
    """
    return phrase.lower().count(letter.lower())
