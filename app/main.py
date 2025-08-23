def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0
    for l in phrase.lower():
        if l == letter.lower():
            counter += 1
    return counter