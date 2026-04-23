def count_occurrences(phrase: str, letter: str) -> int:
    result = 0

    for i in phrase.lower():
        if i == letter.lower():
            result += 1

    return result
