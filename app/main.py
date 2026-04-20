def count_occurrences(phrase: str, letter: str) -> int:

    phrase_lower = phrase.lower()
    letter_lower = letter.lower()

    # Підраховуємо кількість входжень літери в рядок
    return phrase_lower.count(letter_lower)
