def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0

    for chair in phrase:
        if chair.lower() == letter.lower():
            counter += 1

    return counter
