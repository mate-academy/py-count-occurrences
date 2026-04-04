def count_occurrences(phrase: str, letter: str) -> int:
    """
    Implement count_occurrences function that takes phrase and letter
    as arguments and returns number of occurrences of the letter
    in the phrase. The count should be case-insensitive.
    """
    return phrase.lower().count(letter.lower())
