def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0
    for symb in phrase:
        if symb.lower() == letter.lower():
            counter += 1
    return counter
