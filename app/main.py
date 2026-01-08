def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    for L in phrase.lower():
        if L == letter.lower():
            count += 1
    return count
