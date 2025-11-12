def count_occurrences(phrase: str, letter: str) -> int:
    result = 0
    for letters in phrase:
        if letters.lower() == letter.lower():
            result += 1

    return result
