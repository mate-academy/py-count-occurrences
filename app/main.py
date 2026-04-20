def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0
    for one_letter in phrase:
        if one_letter.lower() == letter.lower():
            counter += 1

    return counter
