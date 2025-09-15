def count_occurrences(phrase: str, letter: str) -> int:
    letter_occurrences = 0
    for char in phrase:
        insensitive_char = char.upper()
        if insensitive_char == letter.upper():
            letter_occurrences += 1
    return letter_occurrences
