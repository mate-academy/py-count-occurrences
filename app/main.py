def count_occurrences(phrase: str, letter: str) -> int:
    kol = 0
    for i in phrase:
        if letter.lower() == i.lower():
            kol += 1
    return kol

