def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count the number of times a given letter appears in a phrase, case-insensitive.

    Args:
        phrase(str): The string in which to search for the letter.
        letter(str): The singl character to count (case-insensitive).
    Returns:
        int: The number of occurences of the letter in the phrase.
             If letter is an empty string, returns len(phrase) + 1.
    """
    return phrase.lower().count(letter.lower())
