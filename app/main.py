def count_occurrences(phrase: str, letter: str) -> int:
    count = 0

    for character in phrase:
        if character.lower() == letter.lower():
            count += 1

    return count
