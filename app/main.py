def count_occurrences(phrase: str, letter: str) -> int:
    count = 0

    for char in phrase:
        if char.lower() == letter.lower():
            count += 1

    return count