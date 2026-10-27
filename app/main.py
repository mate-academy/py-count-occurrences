def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count occurrences of a letter in a phrase (case insensitive).

    :param phrase: The phrase to search within.
    :param letter: The letter to count occurrences of.
    :return: The number of occurrences of the letter in the phrase.
    """
    lower_case_phrase = phrase.lower()
    lower_case_letter = letter.lower()
    total = lower_case_phrase.count(lower_case_letter)
    return total
