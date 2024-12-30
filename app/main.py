def count_occurrences(phrase: str, letter: str) -> int:
    """
    count_occurrences("letter", "t") should return 2
    count_occurrences("abc", "a") should return 1
    count_occurrences("abc", "d") should return 0
    count_occurrences("ABC", "a") should return 1
    :param phrase: text to count in it
    :param letter: letter to find
    :return: count occurrences of letter in pharse
    """
    return phrase.lower().count(letter.lower())
