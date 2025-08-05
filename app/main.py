def count_occurrences(phrase: str, letter: str) -> int:
    letter_counter = 0
    for char in phrase.lower():
        if char == letter.lower():
            letter_counter += 1

    return letter_counter
