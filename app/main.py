def count_occurrences(phrase: str, letter: str) -> int:
    """
    :param phrase: A string in which to count occurrences of a letter.
    :param letter: The letter whose occurrences need to be counted
    in the given phrase.
    :return: the number of times the letter appears in the phrase,
    while being case insensitive.
    """

    return phrase.lower().count(letter.lower())
