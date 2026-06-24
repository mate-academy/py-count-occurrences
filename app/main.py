def count_occurrences(phrase: str, letter: str) -> int:
    phrase_lower = phrase.lower()
    letter_lower = letter.lower()
    counter = 0
    for character in phrase_lower:
        if character == letter_lower:
            counter += 1

    return counter
