def count_occurrences(phrase: str, letter: str) -> int:
    counter: int = 0
    for char in phrase:
        if char.lower() == letter.lower():
            counter += 1
    return counter