def count_occurrences(phrase: str, letter: str) -> int:
    """
    Counts the number of times a specific letter appears in a phrase,
    ignoring case sensitivity.

    The function uses Python's built-in string methods for conciseness
    and efficiency.

    :param phrase: The input string to search within.
    :param letter: The single-character string to count occurrences of.
    :return: The total count of the letter in the phrase as an integer.
    """

# First, convert the phrase and the search letter to lowercase.

    phrase_lower = phrase.lower()
    letter_lower = letter.lower()

# Use the built-in .count() method

    return phrase_lower.count(letter_lower)