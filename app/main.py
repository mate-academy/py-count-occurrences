def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count occurrences of a letter or substring in a phrase (case-insensitive).

    :param phrase: The phrase to search within.
    :param letter: The letter (single character) or substring to count.
    :return: The number of occurrences of letter in phrase as an int.
    """
    low_phrase = phrase.lower()
    low_letter = letter.lower()
    return low_phrase.count(low_letter)
