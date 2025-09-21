def count_occurrences(phrase: str, letter: str) -> int:
    """
    implement count_occurrences function:

    It takes a phrase and a letter and calculates number of times
    the letter appears in the phrase. The function case insensitive.

    count_occurrences("letter", "t") == 2
    count_occurrences("abc", "a") == 1
    count_occurrences("abc", "d") == 0
    count_occurrences("ABC", "a") == 1

    :param phrase: phrase to count in it
    :param letter: letter to find occurrences of it
    :return: count occurrences of letter in phrase
    """
    counter = 0
    for char in phrase:
        if char.lower() == letter.lower():
            counter += 1
    return counter
