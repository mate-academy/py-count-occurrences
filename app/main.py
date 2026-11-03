def count_occurrences(phrase: str, letter: str) -> int:
    """Return case-insensitive occurrences of a letter in a phrase."""
    normalized_phrase = phrase.lower()
    normalized_letter = letter.lower()

    return normalized_phrase.count(normalized_letter)
