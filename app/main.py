def count_occurrences(phrase: str, letter: str) -> int:
    if not letter:  # empty string or None
        return 0
    return phrase.lower().count(letter.lower())
