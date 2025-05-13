def count_occurrences(phrase: str, letter: str) -> int:
    return sum(1 if i.lower() == letter.lower() else 0 for i in phrase)
