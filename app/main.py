def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0
    letter = letter.lower()
    for char in phrase.lower():
        if char == letter:
            counter += 1
    return counter

