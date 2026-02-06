def count_occurrences(phrase: str, letter: str) -> int:
    result = 0

    for char in phrase:
        if char == letter:
            result += 1

    return result
