from collections import Counter


def count_occurrences(phrase: str, letter: str) -> int:
    char_counts = Counter(phrase.lower())
    return char_counts.get(letter.lower(), 0)

