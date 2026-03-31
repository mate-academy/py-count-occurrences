def count_occurrences(phrase: str, letter: str) -> int:
    if len(phrase) != 0:
        counter = 0
        for i in phrase:
            if i.lower() == letter.lower():
                counter += 1
    else:
        return 0
    return counter
