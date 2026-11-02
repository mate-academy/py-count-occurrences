def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    for l in phrase:
        if letter.lower() == l.lower():
            count += 1
    return count
