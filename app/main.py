def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0
    for chararacter in phrase:
        if chararacter.lower() == letter.lower():
            counter += 1

    return counter
