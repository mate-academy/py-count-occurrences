def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    for letter1 in phrase.lower():
        if letter1 == letter.lower():
            count += 1
    return count
