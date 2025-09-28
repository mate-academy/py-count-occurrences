def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0
    for quantity in phrase:
        if quantity.lower() == letter.lower():
            counter += 1
    return counter

