def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0
    for symbol in phrase:
        if symbol.lower() == letter.lower():
            counter += 1
    return counter
