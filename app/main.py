def count_occurrences(phrase: str, letter: str) -> int:
    letter_count = 0
    for substring in phrase:
        if letter.upper() == substring.upper():
            letter_count += 1
    return letter_count
