def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count how many times a letter appears in a phrase (case-insensitive).

    :param phrase: The input string to search in
    :param letter: The letter to count
    :return: Number of occurrences of the letter in the phrase
    """
    count = 0

    for char in phrase:
        if char.lower() == letter.lower():
            count += 1

    return count
