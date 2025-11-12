def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    letter = letter.lower()
    for lat in phrase.lower():
        if lat == letter:
            count += 1
    return count
