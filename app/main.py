def count_occurrences(phrase: str, letter: str) -> int:
    count = 0

    for char in phrase:
        if char == letter or char == letter.lower() or char == letter.upper():
            count += 1

    return count
