def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0
    for phr in phrase:
        if phr.lower() == letter.lower():
            counter += 1
    return counter
