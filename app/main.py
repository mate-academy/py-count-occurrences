def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count occurrences of a letter in a phrase (case insensitive).

    :param phrase: The phrase to search within.
    :param letter: The letter to count occurrences of.
    :return: The number of occurrences of the letter in the phrase.
    """
    phrase_lower = phrase.lower()
    letter_lower = letter.lower()
    output = 0

    for l in phrase_lower:
        if l == letter_lower:
            output += 1

    return output
