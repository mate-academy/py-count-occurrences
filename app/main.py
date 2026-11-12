def count_occurrences(phrase: str, letter: str) -> int:
    """Count occurrences of letter in a phrase."""
    return phrase.lower().count(letter.lower())
