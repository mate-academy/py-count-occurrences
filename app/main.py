def count_occurrences(phrase: str, letter: str) -> int:
    """
    Takes a phrase and a letter and returns the number of times
    the letter appears in the phrase, case-insensitive.
    """
    return phrase.lower().count(letter.lower())
