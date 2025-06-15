def count_occurrences(phrase: str, letter: str) -> int:
    letter = letter.lower()
    count = 0
    for ch in phrase.lower():
        if ch == letter:
            count += 1
    return count
