def count_occurrences(phrase: str, letter: str) -> int:
    """
    count occurrences of a letter in a phrase (case insensitive).
    :param phrase: the phrase to search within
    :param letter: the letter to count occurrences of.
    return: the number of occurrences of the letter in the phrase
    """
    return phrase.lower().count(letter.lower())
