def count_occurrences(phrase: str, letter: str) -> int:
    couter = 0
    for character in phrase:
        if character.lower() == letter.lower():
            couter += 1

    return couter
