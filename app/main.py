def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0
    letter = letter.lower()
    for character in phrase.lower():
        if character == letter:
            counter += 1

    return counter