def count_occurrences(phrase: str, letter: str) -> int:
    """
    Liczy, ile razy konkretna litera pojawia się w podanym tekście.
    Wielkość liter nie ma znaczenia (ignoruje się małe i duże litery).

    :param phrase: Pełne zdanie lub tekst, który przeszukujemy.
    :param letter: Litera, którą chcemy policzyć (musi być pojedynczym znakiem).
    :return: Całkowita liczba wystąpień tej litery w tekście.
    """
    return phrase.lower().count(letter.lower())
