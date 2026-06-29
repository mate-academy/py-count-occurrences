def count_occurrences(phrase: str, letter: str) -> int:
    """
    counts occurrences of letter in phrase
    """
    return phrase.lower().count((letter.lower()))
