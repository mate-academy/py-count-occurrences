def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count occurrences of a substring (letter/word) in a phrase (case insensitive).
    
    :param phrase: The phrase to search within.
    :param letter: The substring to count occurrences of.
    :return: The number of occurrences of the substring in the phrase.
    """
    
    # Конвертуємо обидва рядки в нижній регістр для регістронезалежного підрахунку
    lowercase_phrase = phrase.lower()
    lowercase_letter = letter.lower()
    
    # Використовуємо вбудований метод count(), який підтримує підрахунок рядків будь-якої довжини
    return lowercase_phrase.count(lowercase_letter)
