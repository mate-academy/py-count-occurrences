from collections import Counter
def count_occurrences(phrase: str, letter: str) -> int:

    return Counter(phrase.lower())[letter.lower()]
