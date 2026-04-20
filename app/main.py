def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0

    for characters in phrase:
        if characters.lower() == letter.lower():
            counter += 1
    return counter