def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count occurrences of a letter in a phrase (case insensitive).
    :param phrase: The phrase to search within.
    :param letter: The letter to count occurrences of.
    :return: The number of occurrences of the letter in the phrase.
    """

    # Конвертуємо обидва рядки в нижній регістр
    lowercase_phrase = phrase.lower()
    lowercase_letter = letter.lower()

    # Використовуємо вбудований метод count()
    return lowercase_phrase.count(lowercase_letter)
