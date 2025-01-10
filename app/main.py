def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0
    for count in phrase:
        if count.upper() == letter.upper():
            counter += 1
    return counter
