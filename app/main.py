from collections import Counter


def count_occurrences(phrase: str, letter: str) -> int:
    """
        Count occurrences of a letter in a phrase (case insensitive).

        :param phrase: The phrase to search within.
        :param letter: The letter to count occurrences of.
        :return: The number of occurrences of the letter in the phrase.
    """
    char_counts = Counter(phrase.lower())
    return char_counts.get(letter.lower(), 0)

