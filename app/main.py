def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    inputs = list(phrase.lower())
    for _ in inputs:
        if _ == letter.lower():
            count += 1
    return count
