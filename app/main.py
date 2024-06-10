def count_occurrences(phrase: str, letter: str) -> int:
    letter_count = 0
    for char in phrase:
        if char.lower() == letter.lower():
            letter_count += 1
    return letter_count