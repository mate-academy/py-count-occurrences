def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0
    for symbol in phrase.lower():
        if symbol == letter.lower():
            counter += 1
    return counter
