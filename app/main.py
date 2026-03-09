def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0
    letter_lower = letter.lower()
    phrase = phrase.lower()
    for char in phrase:
        if char == letter_lower:
            counter += 1
    return counter
