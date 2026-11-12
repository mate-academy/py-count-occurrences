def count_occurrences(phrase: str, letter: str) -> int:
    count_letter = 0
    for i in phrase.lower():
        if i == letter.lower():
            count_letter += 1
    return count_letter
