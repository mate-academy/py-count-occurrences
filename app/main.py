from cmath import phase


def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    if phrase.lower() in letter.lower() and len(letter) <= 1:
        count += 1
        return count
