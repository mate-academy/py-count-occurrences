def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0
    for char in phrase.lower():
        if char == letter.lower():
            counter += 1
    return counter
