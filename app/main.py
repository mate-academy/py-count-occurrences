def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0
    for phrase in phrase:
        if letter.lower() == phrase.lower():
            counter += 1

    return counter
