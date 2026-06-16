def count_occurrences(phrase: str, letter: str) -> int:
    number = 0
    for char in phrase:
        if char.lower() == letter.lower():
            number += 1
    return number
