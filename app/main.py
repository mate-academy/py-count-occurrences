def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0

    for charakter in phrase:
        if charakter.lower() == letter.lower():
            counter += 1

    return counter
