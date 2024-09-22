def count_occurrences(phrase: str, letter: str) -> int:
    out = 0
    for char in phrase:
        if (char.lower() == letter.lower()):
            out += 1
    return out
