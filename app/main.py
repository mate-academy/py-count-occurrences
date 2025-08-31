from cmath import phase


def count_occurrences(phrase: str, letter: str) -> int:
    if len(letter) != 1:
        return 0

    count = 0
    for letter in phrase:
        if letter.lower() == letter.lower():
            count += 1
    return count
