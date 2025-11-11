def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count occurrences of a letter in a phrase (case insensitive).
    :param phrase: The phrase to search within.
    :param letter: The letter to count occurrences of.
    :return: The number of occurrences of the letter in the phrase.
    """

# First, convert the phrase and the search letter to lowercase.

    phrase_lower = phrase.lower()
    letter_lower = letter.lower()

# Use the built-in .count() method

    return phrase_lower.count(letter_lower)
