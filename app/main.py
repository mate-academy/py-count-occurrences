def count_occurrences(phrase: str, letter: str) -> int:
    count_of_letter = 0  # рахуємо кількість заданних літер у слові
    for i in list(phrase.lower()):  # для кожного елемента слова
        if i == letter.lower():  # задаємо те, з чим порівняти кожен елемент
            count_of_letter += 1  # додаємо +1 до підрахунку кількості літер
    return count_of_letter  # повертаємо результат підрахунків
