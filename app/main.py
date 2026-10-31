def count_occurrences(phrase: str, letter: str) -> int:
    counters = 0
    for char in phrase:
        if char.lower() == letter.lower():
            counters += 1
    return counters
