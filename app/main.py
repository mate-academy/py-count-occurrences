def count_occurrences(phrase: str, letter: str) -> int:
    if len(phrase) == 0 or len(letter) != 1:
        return 0
    if not letter:
        return 0
    return phrase.lower().count(letter.lower())
