def count_occurrences(phrase: str, letter: str) -> int:
    counts = 0
    for char in phrase.lower():
        if char == letter.lower():
            counts += 1
    return counts
