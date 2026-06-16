def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count how many times a letter occurs in a phrase (case-insensitive).

    :param phrase: Input text to search in.
    :param letter: Letter to count.
    :return: Number of occurrences of the letter.
    """

    return phrase.lower().count(letter.lower())
