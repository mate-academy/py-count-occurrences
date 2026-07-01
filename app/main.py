def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count occurrences of a letter in a phrase (case insensitive).
    :param phrase: The phrase to search within.
    :param letter: The letter to count occurrences of.
    :return: The number of occurrences of letter in phrase, case-insensitive.
    """

    counter = 0
    for char in phrase:
        if char.lower() == letter.lower():
            counter += 1
    return counter
