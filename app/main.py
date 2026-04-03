def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    for l in phrase:
        if l in letter.lower() or l in letter.upper():
            count += 1
    return count