def count_occurrences(phrase: str, letter: str) -> int:

    occurrences = 0
    for character in phrase:
        if character.lower() == letter.lower():
            occurrences += 1

    return occurrences
