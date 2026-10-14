def count_occurrences(phrase: str, letter: str) -> int:
    if not phrase or not letter:
        return 0
    target = letter.lower()
    count = 0
    for ch in phrase:
        if ch.lower() == target:
            count += 1
    return count
