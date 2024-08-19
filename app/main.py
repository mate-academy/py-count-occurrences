def count_occurrences(phrase: str, letter: str) -> int:
    """
    Counts the number of occurrences of a given letter in a phrase.
    The count is case insensitive.

    :param phrase: Phrase in which to count occurrences of the letter.
    :param letter: Letter whose occurrences are to be counted.
    :return: The number of occurrences of the letter in the phrase.
    """
    number_of_letter = 0
    # Перетворення фрази та букви в нижній регістр
    phrase = phrase.lower()
    letter = letter.lower()

    # Перевірка на те, що letter є однією буквою
    if len(letter) != 1:
        raise ValueError("The 'letter' parameter should be a single character.")

    # Підрахунок кількості входжень букви у фразу
    for char in phrase:
        if char == letter:
            number_of_letter += 1

    return number_of_letter


# Отримання вводу від користувача
phrase = input("Enter a phrase: ").lower()
letter = input("Enter a letter: ").lower()

# Перевірка на те, що letter є однією буквою
if len(letter) != 1:
    raise ValueError("The 'letter' parameter should be a single character.")

# Підрахунок входжень та виведення результату
result = count_occurrences(phrase, letter)
print(f"The letter '{letter}' occurs {result} times in the phrase.")
