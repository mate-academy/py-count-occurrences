def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    for lett in phrase.upper():
        if lett == letter.upper():
            count += 1
    return count
