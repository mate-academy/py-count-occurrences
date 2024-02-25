from collections import Counter


def count_occurrences(phrase: str, letter: str) -> int:
    phrase = phrase.lower()
    letter = letter.lower()
    count = Counter(phrase)[letter]
    return count
