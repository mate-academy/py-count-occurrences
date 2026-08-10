def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0
    for a in phrase:
        if a.lower() == letter.lower():
            counter += 1
    return counter
