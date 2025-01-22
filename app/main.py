def count_occurrences(phrase: str, letter: str) -> int:
    total = 0
    for letter_new in phrase:
        if letter.lower() == letter_new.lower():
            total += 1
    return total
