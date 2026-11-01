def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count occurrences of a letter in a phrase (case insensitive).

    :param phrase: The phrase to search within.
    :param letter: The letter to count occurrences of.
    :return: The number of occurrences of the letter in the phrase.
    """
    if phrase.find(letter.lower()) > -1 or phrase.find(letter.upper()) > -1:
        return phrase.count(letter.lower()) + phrase.count(letter.upper())
    return 0
