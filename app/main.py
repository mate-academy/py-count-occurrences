def count_occurrences(phrase: str, letter: str) -> int:
    for char in phrase:
        count = 0
        if char.lower() == letter.lower():
            count += 1
    return count
