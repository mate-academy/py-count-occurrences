def count_occurrences(phrase: str, letter: str) -> int:
    return sum(map(lambda c: 1 if c.lower() == letter.lower() else 0, phrase))
