def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    phrase_lower = phrase.lower()
    letter_lower = letter.lower()
    for char in phrase_lower:
        if char == letter_lower:
            count = count + 1
    return count
