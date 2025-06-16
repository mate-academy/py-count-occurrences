def count_occurrences(phrase: str, letter: str) -> int:
    letter = letter.lower()

    counter = 0
    for char in phrase.lower():
        if letter == char:
            counter += 1

    return counter
