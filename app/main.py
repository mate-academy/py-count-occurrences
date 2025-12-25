def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0
    for ph_letter in phrase:
        if ph_letter.lower() == letter.lower():
            counter += 1
    return counter
