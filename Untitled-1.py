def count_occurrences(phrase: str, letter: str) -> int:
    letter_count = 0
    for all_letters in phrase:
        if letter.lower() == all_letters:
            letter_count += 1
    return letter_count