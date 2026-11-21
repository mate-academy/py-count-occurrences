def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0
    for cher in phrase:
        if cher.lower() == letter.lower():
            counter += 1
    return counter
