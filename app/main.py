def count_occurrences(phrase: str, letter: str) -> int:
    """
    Implement count_occurrences function:

    It takes a phrase and a letter and calculates the number of times
    the letter appears in the phrase. The function is case insensitive.

    count_occurrences("letter", "t") should return 2
    count_occurrences("abc", "a") should return 1
    count_occurrences("abc", "d") should return 0
    count_occurrences("ABC", "a") should return 1

    :param phrase: The phrase to search within.
    :param letter: The letter to count occurrences of.
    :return: The number of occurrences of the letter in the phrase.
    """
    return phrase.lower().count(letter.lower())
