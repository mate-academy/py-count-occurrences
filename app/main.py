def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0  # ініціалізація лічильника

    for char in phrase:  # перебір символів у рядку
        if char.lower() == letter.lower():  # перевірка регістру
            counter += 1  # збільшуємо лічильник

    return counter  # повертаємо результат після циклу
