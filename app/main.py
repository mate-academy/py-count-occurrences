def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count how many times a letter appears in a phrase (case insensitive).

    :param phrase: The string in which to count occurrences.
    :param letter: The letter to search for.
    :return: The number of times the letter appears in the phrase.
    """
    return phrase.lower().count(letter.lower())
