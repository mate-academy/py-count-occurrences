def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count occurrences of a letter in a phrase (case insensitive).

    :param phrase: The phrase to search within.
    :param letter: The letter to count occurrences of.
    :return: The number of occurrences of the letter in the phrase.
    """
    if len(letter) != 1:
        raise ValueError("The 'letter' parameter must be a single character.")
    return phrase.lower().count(letter.lower())
