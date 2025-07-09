def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    for char in phrase.lower():
        if char == letter.lower():
            count += 1
    return count
