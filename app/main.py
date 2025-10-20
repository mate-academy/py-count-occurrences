def count_occurrences(phrase: str, letter: str) -> int:
    """
    :param phrase:
    :param letter:
    :return: count of occurrences of letter in phrase
    """
    return phrase.lower().count(letter.lower())
