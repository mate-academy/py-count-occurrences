def count_occurrences(phrase: str, letter: str) -> int:
    """ Return the number of times the letter appears in the phrase"""
    return phrase.lower().count(letter.lower())
