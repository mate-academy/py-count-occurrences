def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0

    for character in phrase:
        if character.upper() == letter.upper():
            counter += 1

    return counter
