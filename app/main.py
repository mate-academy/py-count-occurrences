"""Contains a function to perform a case insensitive search in a phrase."""


def count_occurrences(phrase: str, letter: str) -> int:
    """Perform case instensitive search of a letter in a phrase.

    Args:
    phrase - a phrase to perform a search
    letter - a letter to be searched in the phrase

    Returns:
    The total amount of the letter occurrences in the phrase

    Raises:
    A value error if the phrase or the letter are not a string
    """
    if not isinstance(phrase, str):
        raise ValueError("Phrase type should be a string")

    if not isinstance(letter, str):
        raise ValueError("Letter type should be a string")

    return phrase.lower().count(letter.lower())
