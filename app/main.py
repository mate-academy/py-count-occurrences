def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    for sign in phrase:
        if sign.lower() == letter.lower():
            count += 1
    return count
