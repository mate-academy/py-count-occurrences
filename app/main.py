def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0
    for charachter in phrase:
        if charachter.lower() == letter.lower():
            counter += 1

    return counter
