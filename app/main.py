def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count occurrences of a letter (or substring) in a phrase
    (case insensitive).

    :param phrase: The phrase to search within.
    :param letter: The letter (or substring) to count
        occurrences of.
    :return: The number of occurrences of the letter (or
        substring) in the phrase.
    """
    return phrase.lower().count(letter.lower())
