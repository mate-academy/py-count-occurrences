def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0
    for char in phrase:
        if char.upper() == letter.upper():
            counter += 1
    return counter
