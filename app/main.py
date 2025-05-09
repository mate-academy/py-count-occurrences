def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0
    for character in phrase:
        if character == letter.lower():
            counter += 1
        return counter