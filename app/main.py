def count_occurrences(phrase: str, letter: str) -> int:
    """
        Counts the number of times a letter appears in a phrase, ignoring case.

        :param phrase: The string to search within.
        :param letter: The letter to count occurrences of (single character, case-insensitive).
        :return: The integer count of occurrences.
    """
    return phrase.lower().count(letter.lower())
