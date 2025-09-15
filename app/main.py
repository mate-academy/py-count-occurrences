def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    letter = letter.lower()
    for char in phrase:
        if char.lower() == letter:
            count += 1
    return count
