def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    for character in phrase:
        if letter.lower() == character.lower():
            count += 1
    return count
