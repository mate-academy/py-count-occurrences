def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0
    for i in phrase:
        if i.lower() == letter.lower():
            counter += 1
    return counter
