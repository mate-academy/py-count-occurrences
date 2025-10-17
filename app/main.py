def count_occurrences(phrase: str, letter: str) -> int:
    number_of_occurrences = 0
    for char in phrase:
        if char.lower() == letter.lower():
            number_of_occurrences += 1

    return number_of_occurrences

