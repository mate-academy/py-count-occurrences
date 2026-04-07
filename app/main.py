def count_occurrences(phrase: str, letter: str) -> int:

    counter = 0
    for item in phrase:
        if letter.lower() == item.lower():
            counter += 1

    return counter
