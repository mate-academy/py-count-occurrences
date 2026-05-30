def count_occurrences(phrase: str, letter: str) -> int:
    k = 0

    for i in phrase:
        if i.lower() == letter.lower():
            k += 1

    return k
