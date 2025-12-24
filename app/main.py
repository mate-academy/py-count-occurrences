def count_occurrences(phrase: str, letter: str) -> int:
    letter_count = 0

    for phrase_char in phrase:
        if phrase_char.lower() == letter.lower():
            letter_count += 1

    return letter_count
