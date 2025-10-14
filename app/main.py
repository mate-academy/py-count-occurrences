

def count_occurrences(phrase: str, letter: str) -> int:
    """
    Counts the occurrences of a specific letter in a given phrase, ignoring case.

    This function takes a phrase and a letter, both as string inputs, and determines
    how many times the specified letter appears in the phrase, regardless of case.

    :param phrase: The string in which to search for the occurrences of the letter.
    :param letter: The letter whose occurrences need to be counted in the phrase.
    :return: The number of times the specified letter appears in the given phrase.
    :rtype: int
    """
    return phrase.lower().count(letter.lower())
