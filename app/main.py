def count_occurrences(phrase: str, letter: str) -> int:
    """Count occurrences of a letter in a phrase (case insensitive).
    :param phrase: The phrase in which to count occurrences.
    :param letter: The letter to count within the phrase.
    :return: The number of times the letter appears in the phrase.
    """
    counter = 0
    for char in phrase.lower():
        if char == letter.lower():
            counter += 1
    return counter
