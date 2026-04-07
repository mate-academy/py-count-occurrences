def count_occurrences(phrase: str, letter: str) -> int:

    counter = 0
    for character in phrase:
        if letter.lower() == character.lower():
            counter += 1

    return counter
