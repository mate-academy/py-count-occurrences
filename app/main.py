def count_occurrences(phrase: str, letter: str) -> int:
    result = 0
    for c in phrase:
        if c.lower() == letter.lower() or c.upper() == letter.upper():
            result += 1
    return result

