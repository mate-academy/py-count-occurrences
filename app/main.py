def count_occurrences(phrase: str, letter: str) -> int:
    occurrences = 0

    for char in phrase:
        if char.lower() == letter.lower():
            occurrences += 1

    return occurrences
