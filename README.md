def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count occurrences of a letter in a phrase (case insensitive).

    :param phrase: The phrase to search within.
    :param letter: The letter to count occurrences of.
    :return: The number of occurrences of the letter in the phrase.
    """
    return phrase.lower().count(letter.lower())

# Test cases
print(count_occurrences("letter", "t"))  # Output: 2
print(count_occurrences("abc", "a"))     # Output: 1
print(count_occurrences("abc", "d"))     # Output: 0
print(count_occurrences("ABC", "a"))     # Output: 1
