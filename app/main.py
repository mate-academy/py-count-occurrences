def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    for alfa in phrase:
        if alfa.lower() == letter.lower():
            count += 1
    return count

