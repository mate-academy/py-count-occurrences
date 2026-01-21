from collections import Counter
from subprocess import check_output


def count_occurrences(phrase: str, letter: str) -> int:
    return Counter(phrase.lower())[letter.lower()]

