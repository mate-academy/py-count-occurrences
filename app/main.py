def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count occurrences of a letter in a phrase.

    :param phrase: The phrase to search within.
    :param letter: The letter to count occurrences of.
    :return: The number of occurrences of the letter in the phrase.
    """
    counter = 0

    for letter_phrase in phrase:
        if letter_phrase.lower() == letter.lower():
            counter += 1
    return counter
