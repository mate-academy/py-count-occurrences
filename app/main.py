def count_occurrences(phrase: str, letter: str) -> int:
    quantity = 0

    for char in phrase:
        if char.lower() == letter.lower():
            quantity += 1

    return quantity
