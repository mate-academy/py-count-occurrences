def count_occurrences(phrase: str, substring: str) -> int:
    """
    Count occurrences of a substring in a phrase (case insensitive).
    :param phrase: The phrase to search within.
    :param substring: The substring to count occurrences of.
    :return: The number of occurrences of the substring in the phrase.
    """
    return phrase.lower().count(substring.lower())
