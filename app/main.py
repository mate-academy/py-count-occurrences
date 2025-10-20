def count_occurrences(phrase: str, letter: str) -> int:
    """
    :param phrase:
    :param letter:
    :return: count of occurrences of letter in phrase
    """
    count = 0

    for charecter in phrase:
        if charecter.lower() == letter.lower():
            count += 1

    return count
