def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    for phrases in phrase:
        if phrases.lower() == letter.lower():
            count += 1
    return count
