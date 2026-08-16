def count_occurrences(phrase: str, letter: str) -> int:
    count = 0

    for character in phrase.lower():
        if character == letter.lower():
            count += 1

    return count
