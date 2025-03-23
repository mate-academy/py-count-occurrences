def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    for symbol in phrase:
        if symbol.lower() == letter.lower():
            count += 1
    return count
