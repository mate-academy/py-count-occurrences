def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    for item in phrase:
        if letter.lower() in item.lower():
            count = count + 1
    return count
