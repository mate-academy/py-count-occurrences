def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count the occurrences of a letter in a given phrase.

    :param phrase: The phrase to search within.
    :param letter: The letter to count.
    :return: The number of occurrences of the letter in the phrase.
    """
    return phrase.lower().count(letter.lower())
