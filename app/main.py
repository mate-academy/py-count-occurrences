def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    for char in phrase:
        if letter.lower() == char.lower():
            count += 1
    return count
