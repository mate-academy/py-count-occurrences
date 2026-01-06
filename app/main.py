def count_occurrences(phrase: str, letter: str) -> int:
    low_phrase = phrase.lower()
    low_letter = letter.lower()
    letter_count = low_phrase.count(low_letter)
    return letter_count

    pass
