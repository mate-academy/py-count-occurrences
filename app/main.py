def count_occurrences(phrase: str, letter: str) -> int:
    result = 0
    for symb in phrase:
        if symb.lower() == letter.lower():
            result += 1
    return result
