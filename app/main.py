def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0

    for chad in phrase:
        if chad.lower() == letter.lower():
            counter += 1

    return counter
