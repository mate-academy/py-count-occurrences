def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0
    for lit in phrase:
        if lit.lower() == letter.lower():
            counter += 1
    return counter
