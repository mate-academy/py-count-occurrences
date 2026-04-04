def count_occurrences(phrase: str, letter: str) -> int:
    # Приводимо всі символи до нижнього регістру, що б функція не була чутлива
    phrase_lower = phrase.lower()
    letter_lower = letter.lower()

    # Використовуємо вбудований метод count для підрахунку
    return phrase_lower.count(letter_lower)
