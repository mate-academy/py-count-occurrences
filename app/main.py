def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count occurrences of a letter in a phrase (case insensitive).

    count_occurrences("letter", "t") should return 2
    count_occurrences("abc", "a") should return 1
    count_occurrences("abc", "d") should return 0
    count_occurrences("ABC", "a") should return 1

    :param phrase: The phrase to search within.
    :param letter: The letter to count occurrences of.
    :return: The number of occurrences of the letter in the phrase.
    """

    return phrase.lower().count(letter.lower())
