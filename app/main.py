def count_occurrences(phrase: str, letter: str) -> int:
    counts = 0
    letter = letter.lower()
    for char in phrase.lower():
        if char == letter:
            counts += 1
    return counts
