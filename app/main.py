def count_occurrences(phrase: str, letter: str) -> int:
    """
    Zlicza liczbę wystąpień podanej litery w tekście.

    Porównanie jest niewrażliwe na wielkość liter (case-insensitive).

    Args:
        phrase (str): Tekst, w którym wyszukiwane są wystąpienia.
        letter (str): Litera, której liczba wystąpień ma zostać policzona.

    Returns:
        int: Liczba wystąpień litery w podanym tekście.
    """
    counter = 0

    for charakter in phrase:
        if charakter.lower() == letter.lower():
            counter += 1

    return counter
