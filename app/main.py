def count_occurrences(phrase: str, letter: str) -> int:
    """
    Zlicza wystąpienia danego znaku w podanym tekście (bez rozróżniania wielkości liter).

    :param phrase: Tekst, w którym ma być wyszukiwany znak.
    :param letter: Znak, którego wystąpienia mają zostać policzone.
    :return: Liczba wystąpień danego znaku w tekście.
    """
    if not phrase or not letter:
        return 0
    return phrase.lower().count(letter.lower())
