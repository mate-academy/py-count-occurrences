def count_occurrences(phrase: str, letter: str) -> int:
    lower = phrase.lower()
    return lower.count(letter.lower())
