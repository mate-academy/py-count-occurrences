def count_occurrences(phrase: str, letter: str) -> int:
    """
    Function which counts number of letters
    :param phrase:
    :param letter:
    :return:
    """
    return phrase.lower().count(letter.lower())
