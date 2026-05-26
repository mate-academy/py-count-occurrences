def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count occurrences of a letter in a phrase (case insensitive).

    :param phrase: The phrase to search within.
    :param letter: The letter (or substring) to count occurrences of.
    :return: The number of occurrences of `letter` in `phrase` as an int.
    """
    return phrase.lower().count(letter.lower())
