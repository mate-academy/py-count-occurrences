def count_occurrences(phrase: str, letter: str) -> int:
    result = 0
    for sign in phrase:
        if sign.lower() == letter.lower():
            result += 1
    return result
