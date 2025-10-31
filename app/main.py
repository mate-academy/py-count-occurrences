def count_occurrences(phrase, letter):
    # Перетворюємо весь текст у маленькі літери, 
    # щоб "A" і "a" рахувалися як однакові
    phrase = phrase.lower()

    # Так само робимо з літерою, яку шукаємо
    letter = letter.lower()

    # Рахуємо, скільки разів ця літера зустрічається у тексті
    return phrase.count(letter)
