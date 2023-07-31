def count_occurrences(phrase: str, letter: str) -> int:
    """
    :param phrase: phrase to count in it
    :param letter: letter to find occurrences of it
    :return: count occurrences of letter in phrase
    """
    count_of_letters = 0

    for char in phrase:
        if char.lower() == letter.lower():
            count_of_letters += 1

    return count_of_letters
