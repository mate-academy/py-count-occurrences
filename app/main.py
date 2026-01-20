def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count occurrences of a letter in a phrase (case insensitive).

    :param phrase: The phrase to search within.
    :param letter: The letter (or substring) to count occurrences of.
    :return: The number of occurrences of the letter in the phrase as an int.
    """
    lower_phrase = phrase.lower()
    counter = lower_phrase.count(letter.lower())
    return counter
