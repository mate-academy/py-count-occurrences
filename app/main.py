def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count how many times the given letter appears in the phrase,
    ignoring letter case

    :param phrase: string in which we search a letters
    :param letter: letter to count
    :return: sum of letters which we count
    """
    counter = 0
    for char in phrase:
        if char.lower() == letter.lower():
            counter += 1

    return counter
