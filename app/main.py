def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    for i in phrase.lower():
        if letter.lower() == i.lower():
            count += 1
    return count
