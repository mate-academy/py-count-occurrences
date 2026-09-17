def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0
    for i in phrase.lower():
        if i == letter.lower():
            counter += 1
    return counter
