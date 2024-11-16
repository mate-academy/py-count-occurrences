def count_occurrences(phrase: str, letter: str) -> int:
    """
    Подсчитывает количество вхождений буквы в строку (регистронезависимо).

    :param phrase: Строка, в которой нужно искать букву.
    :param letter: Буква, чьи вхождения нужно подсчитать.
    :return: Количество вхождений буквы в строке.
    """
    # Проверка корректности входных данных
    if not isinstance(phrase, str) or not isinstance(letter, str):
        raise ValueError(
            "Оба параметра, phrase и letter, должны быть строками."
        )
    if len(letter) != 1:
        raise ValueError("Параметр letter должен быть одним символом.")

    # Приведение строки и буквы к нижнему регистру и подсчет
    return phrase.lower().count(letter.lower())


# Примеры использования
print(count_occurrences("letter", "t"))  # 2
print(count_occurrences("abc", "a"))     # 1
print(count_occurrences("abc", "d"))     # 0
print(count_occurrences("ABC", "a"))     # 1
