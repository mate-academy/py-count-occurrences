def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    for let in phrase.lower():
        if let == letter.lower():
            count += 1
    return count
