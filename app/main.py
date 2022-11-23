def count_occurrence(phrase: str, letter: str) -> int:
    """
    Implement count_occurrences function:

    it takes a phrase and a letter and calculates the number of times
    the letter appears in the phrase. The function is case insensitive.

    count_occurrence("letter", "t") == 2
    count_occurrence("abc", "a") == 1
    count_occurrence("abc", "d") == 0
    count_occurrence("ABC", "a") == 1

    :param phrase: phrase to count in it
    :param letter: letter to find occurrences of it
    :return: count occurrences of letter in phrase
    """
    phrase_lower = phrase.lower()
    counter = phrase_lower.count(letter.lower())
    return counter
