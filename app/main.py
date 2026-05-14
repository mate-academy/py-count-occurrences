def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count how many times a given letter appears in a phrase,
    case-insensitively.

    :param phrase: The text in which to count the letter occurrences.
    :param letter: The letter to count.
    :return: The number of times the letter appears in the phrase.
    """
    return phrase.lower().count(letter.lower())
