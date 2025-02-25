def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0
    for count in phrase:
        if count.lower() == letter.lower():
            counter += 1
    return counter
