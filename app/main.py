def count_occurrences(phrase: str, letter: str) -> int:
    count = 0

    for leter in phrase:
        if leter.lower() == letter.lower():
            count += 1

    return count
