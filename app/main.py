def count_occurrences(phrase: str, letter: str) -> int:
    """
    :param phrase:
    :param letter:
    :return: count of occurrences of letter in phrase
    """
    count = 0

    for character in phrase:
        if character.lower() == letter.lower():
            count += 1

    return count
