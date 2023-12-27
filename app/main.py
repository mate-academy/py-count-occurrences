def count_occurrences(phrase: str, letter: str) -> int:
    # Перетворюємо обидва вхідні аргументи у нижній регістр для порівняння
    phrase = phrase.lower()
    letter = letter.lower()

    # Лічильник для зберігання кількості входжень літери
    count = 0

    # Перебираємо кожен символ у фразі
    for char in phrase:
        if char == letter:
            count += 1

    return count
