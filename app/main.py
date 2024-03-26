def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count the occurrences of a letter in a phrase.

    :param phrase: The input phrase.
    :param letter: The letter to count occurrences of.
    :return: The count of occurrences of the letter in the phrase.
    """
    return sum(1 for char in phrase if char.lower() == letter.lower())


a = 123
b = []
c = "Hi!"
d = [1, 2]


sorted_variables = {
    "mutable": [],
    "immutable": []
}


def count_letter(phrase, letter):
    return sum(1 for char in phrase if char.lower() == letter.lower())
