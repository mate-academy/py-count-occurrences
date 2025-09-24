def count_occurrences(phrase: str, letter: str) -> int:
    return sum(map(lambda x: 1 if x.lower() == letter.lower() else 0, phrase))
