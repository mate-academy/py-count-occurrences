def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count occurrences of a substring in a phrase (case insensitive).

    :param phrase: The phrase to search within.
    :param letter: The substring to count occurrences of.
    :return: The number of occurrences of the substring in the phrase.
    """

    # Convert both strings to lower case
    lowercase_phrase = phrase.lower()
    lowercase_letter = letter.lower()

    # Use the built-in count() method
    return lowercase_phrase.count(lowercase_letter)
