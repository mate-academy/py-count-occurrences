def count_occurrences(phrase: str, letter: str) -> int:
    phrase = phrase.lower()
    letter = letter.lower()

    counter = 0
    for char in phrase:
        if char.lower() == letter.lower():
            counter += 1
    return counter