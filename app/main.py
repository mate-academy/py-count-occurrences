def count_occurrences(phrase: str, letter: str) -> int:
    """
    Підраховує кількість входжень вказаної літери у фразі, незалежно від регістру.

    Параметри:
        phrase (str): Рядок, у якому здійснюється пошук.
        letter (str): Літера, кількість входжень якої потрібно підрахувати.

    Повертає:
        int: Кількість входжень літери у фразі (без урахування регістру).

    Приклад:
        >>> count_occurrences("Hello World", "l")
        3
        >>> count_occurrences("Apple", "A")
        1
    """
    return phrase.lower().count(letter.lower())
