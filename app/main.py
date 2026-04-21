def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count occurrences of a letter in a phrase (case insensitive).
    :param phrase: The phrase to search within.
    :param letter: The letter to count occurrences of.
    :return: The number of occurrences of the letter in the phrase.
    """
    lowercase_phrase = phrase.lower()
    lowercase_letter = letter.lower()
    return lowercase_phrase.count(lowercase_letter)


# Examples
print(count_occurrences("letter", "t"))
print(count_occurrences("abc", "a"))
print(count_occurrences("abc", "d"))
print(count_occurrences("ABC", "a"))
