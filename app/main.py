def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count occurrences of a letter in a phrase (case-insensitive).

    :param phrase: The phrase to search within.
    :param letter: The letter to count occurrences of.
    :return: The number of occurrences of the letter in the phrase.
    """
    # Normalize both the phrase and the letter
    # to lowercase for case-insensitive comparison.

    phrase_lower = phrase.lower()
    letter_lower = letter.lower()

    # Count the occurrences of the letter in the phrase.
    return phrase_lower.count(letter_lower)
