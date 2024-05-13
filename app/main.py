def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    for lets in phrase:
        if lets.upper() == letter.upper():
            count += 1
    return count
