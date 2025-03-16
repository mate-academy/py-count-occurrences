def count_occurrences(phrase: str, letter: str) -> int:
    couter = 0
    for char in phrase:
        if char.lower() == letter.lower():
            couter += 1
    return couter
