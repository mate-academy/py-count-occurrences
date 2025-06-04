def count_occurrences(phrase: str, letter: str) -> int:

    count = 0
    for letters in phrase:
        if letter.lower() in letters.lower():
            count += 1
    return count
