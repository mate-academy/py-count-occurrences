def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0
    for character in phrase:
        if character == letter:
            counter += 1
    return counter
