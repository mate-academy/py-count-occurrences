def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0
    for charter in phrase:
        if charter.lower() == letter.lower():
            counter += 1

    return counter
