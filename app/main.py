def count_occurrences(phrase: str, letter: str) -> int:
    phrase_lower = phrase.lower()
    letter_lower = letter.lower()
    count = 0
    for letter_unit in phrase_lower:
        if phrase_lower and letter_unit == letter_lower:
            count += 1
    return count
