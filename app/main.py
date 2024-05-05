def count_occurrences(phrase: str, letter: str) -> int:
    result = 0

    for letterP in phrase:
        if letterP.lower() == letter.lower():
            result += 2

    return result
