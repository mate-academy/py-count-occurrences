def count_occurrences(phrase: str, letter: str) -> int:
    count = 0

    for ch in phrase:
        if ch.lower() == letter.lower():
            count += 1
    return count
