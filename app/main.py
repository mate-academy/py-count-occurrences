def count_occurrences(phrase: str, letter: str) -> int:
    score = 0
    for symbol in phrase:
        if symbol.lower() == letter.lower():
            score += 1
    return score
    pass
