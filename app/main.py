def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count the occurrences of a letter in a phrase.

    :param phrase: The input phrase.
    :param letter: The letter to count occurrences of.
    :return: The count of occurrences of the letter in the phrase.
    """
    return sum(1 for char in phrase if char.lower() == letter.lower())
# Создаем несколько переменных разных типов


a = 123
b = []
c = "Hi!"
d = [1, 2]

# Создаем словарь для сортировки переменных по их типу
sorted_variables = {
    "mutable": [],      # Для изменяемых (mutable) переменных
    "immutable": []     # Для неизменяемых (immutable) переменных
}


def count_letter(phrase, letter):
    return sum(1 for char in phrase if char.lower() == letter.lower())
