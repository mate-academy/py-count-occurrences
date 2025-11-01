def count_occurrences(phrase: str, letter: str) -> int:
    """
    Рахує кількість входжень символу `letter` у рядку `phrase`, незалежно від регістру.

    Parameters:
        phrase (str): Рядок, у якому потрібно виконати пошук.
        letter (str): Символ, кількість входжень якого потрібно знайти.

    Returns:
        int: Кількість входжень символу у рядку.

    Raises:
        ValueError: Якщо параметр `letter` не є одним символом.
    """

    if len(letter) != 1:
        raise ValueError("Параметр 'letter' повинен бути одним символом")

    return phrase.lower().count(letter.lower())
