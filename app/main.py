def count_occurrences(phrase: str, letter: str) -> int:
    if not letter:
        return 0

    if len(letter) != 1:
        raise ValueError("Parameter 'letter' must be a single character")

    return phrase.lower().count(letter.lower())
