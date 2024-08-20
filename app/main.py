def count_occurrences(phrase: str, letter: str) -> int:
    letter_count = 0
    phrase = phrase.lower()
    letter = letter.lower()
    for char in phrase:
        if char == letter:
            letter_count += 1
    return letter_count
