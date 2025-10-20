def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count the occurrences of letter in phrase.
    :param phrase:
    :param letter:
    :return:
    """
    return phrase.lower().count(letter.lower())
