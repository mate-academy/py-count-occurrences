def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    for charm in phrase:
        if charm.lower() == letter.lower():
            count += 1
    return count
