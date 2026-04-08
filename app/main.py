def count_occurrences(phrase: str, letter: str) -> int:
    """
    Підрахунок зустрічей літери у фразі (без ремінстру).
    :param phrase: Рядок, в якому шукаємо літеру.
    :type phrase: str
    :param letter: Літера для підрахунку (очікується рядок довжини 1).
    :type letter: str
    :return: Кількість входжень літери у фразі (інтове значення).
    :rtype: int
    """
    return phrase.lower().count(letter.lower())
