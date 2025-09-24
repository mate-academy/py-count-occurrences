def count_occurrences(phrase: str, letter: str) -> int:
    return sum(map(lambda w: 1 if w.lower() == letter.lower() else 0, phrase))
