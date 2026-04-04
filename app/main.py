def count_occurrences(phrase: str, letter: str) -> int:
    """
    :param phrase: Описание
    :type phrase: str
    :param letter: Описание
    :type letter: str
    :return: Описание
    :rtype: int
    """
    return phrase.lower().count(letter.lower())
