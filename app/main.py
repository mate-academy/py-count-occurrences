def count_occurrences(phrase: str, letter: str) -> int:
    """
    Рахує кількість входжень символу `letter` у рядку `phrase`, незалежно від регістру.
    """

    # Перевірка: letter має бути одним символом
    if len(letter) != 1:
        raise ValueError("Параметр 'letter' повинен бути одним символом")

    # Приводимо все до нижнього регістру і рахуємо кількість входжень
    return phrase.lower().count(letter.lower())
