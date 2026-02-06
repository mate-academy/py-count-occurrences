def count_occurrences(phrase: str, letter: str) -> int:
    result = 0

    for char in phrase:
        if char.lower() == letter.lower():
            result += 1

    return result
