def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count occurrences of a letter in a phrase (case insensitive).

    :param phrase: The phrase to search within.
    :param letter: The letter to count occurrences of the letter.
    :return: The number of occurrences  .
    """
    counter = 0
    for count in phrase:
        if count.lower() == letter.lower():
            counter += 1
    return counter

