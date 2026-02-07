def count_occurrences(phrase: str, letter: str) -> int:
    if letter:
        return 0
    if len(letter) != 1:
        raise ValueError("letter must be a single character")
    return phrase.lower().count(letter.lower())
