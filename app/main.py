def count_occurrences(phrase: str, letter: str) -> int:

    counter = 0
    for har in phrase:
        if har.lower() == letter.lower():
            counter += 1
    return counter
