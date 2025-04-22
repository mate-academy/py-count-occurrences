def count_occurrences(phrase: str, letter: str) -> int:
    score = 0
    for char in phrase:
        if char.lower() == letter.lower():
            score += 1

    return score
