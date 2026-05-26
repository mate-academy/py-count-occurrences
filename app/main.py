def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count occurrences of a letter in a phrase (case insensitive).

    :param phrase: The phrase to search within.
    :param letter: The letter to count occurrences of.
    :return: The number of occurrences of the letter in the phrase.
    """
    if not isinstance(letter, str) or len(letter) != 1:
        raise ValueError("letter must be a single character string")

    return phrase.lower().count(letter.lower())
