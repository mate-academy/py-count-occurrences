def count_occurrences(phrase: str, letter: str) -> int:
    """
       Підрахунок входжень літери у рядку (без врахування регістру).

       :param phrase: Рядок, у якому потрібно шукати.
       :param letter: Літера, кількість входжень якої потрібно підрахувати.
       :return: Кількість входжень літери у рядку.
       """

    phrase_lower = phrase.lower()
    letter_lower = letter.lower()


    return phrase_lower.count(letter_lower)

