def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    for i in phrase:
        if i.lower() == letter.lower():
            count += 1
    return count

