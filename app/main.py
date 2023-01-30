def count_occurrences(phrase: str, letter: str) -> int:
    """
    Implement count_occurrences function:

    It takes a phrase and a letter and calculates the number of times
    the letter appears in the phrase. The function is case insensitive.

    count_occurrences("letter", "t") == 2
    count_occurrences("abc", "a") == 1
    count_occurrences("abc", "d") == 0
    count_occurrences("ABC", "a") == 1

    :param phrase: phrase to count in it
    :param letter: letter to find occurrences of it
    :return: count occurrences of letter in phrase
    """

    count_letter = 0

    for i in phrase.lower():
        if i == letter.lower():
            count_letter += 1
    return count_letter


print(count_occurrences("letter", "t"))
print(count_occurrences("abc", "a"))
print(count_occurrences("abc", "d"))
print(count_occurrences("ABC", "a"))
