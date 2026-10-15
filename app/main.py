def count_occurrences(phrase: str, letter: str) -> int:
    """
    Підрахунок кількості входжень літери у фразу (без урахування регістру).

    :param phrase: Фраза для пошуку всередині неї.
    :param letter: Літера, кількість входжень якої потрібно порахувати.
    :return: Кількість входжень літери у фразу.
    """
    return phrase.lower().count(letter.lower())


# Приклади використання та перевірки:
if __name__ == "__main__":
    print(count_occurrences("letter", "t"))  # Виведе: 2
    print(count_occurrences("abc", "a"))     # Виведе: 1
    print(count_occurrences("abc", "d"))     # Виведе: 0
    print(count_occurrences("ABC", "a"))     # Виведе: 1

