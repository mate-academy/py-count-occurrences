def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count the occurrences of a letter in a phrase ( case-insensitive)
    :param phrase: The phrase to search to within
    :param letter: The letter to count occurrences of
    :return: Yhe number of time the letter appears in the phrase
    """
    return phrase.lower().count(letter.lower())
    pass
