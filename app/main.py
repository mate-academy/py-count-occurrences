def count_occurrences(phrase: str, letter: str) -> int:
    result = 0
    for char in phrase.upper():
        if char == letter.upper():
            result += 1
    return result
    pass
