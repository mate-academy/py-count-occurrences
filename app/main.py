def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0
    for element in phrase.lower():
        if element == letter.lower():
            counter += 1

    return counter
