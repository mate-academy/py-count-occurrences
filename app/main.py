def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    for el in phrase:
        if el.lower() == letter.lower():
            count += 1
    return count
