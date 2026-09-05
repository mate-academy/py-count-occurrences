def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0
    for charackter in phrase:
        if charackter.lower() == letter.lower():
            counter += 1

    return counter
