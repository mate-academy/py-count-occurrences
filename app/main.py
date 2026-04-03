def count_occurrences(phrase: str, letter: str) -> int:
    lower_phrase = phrase.lower()
    lower_letter = letter.lower()
    letter_count = lower_phrase.count(lower_letter)
    return letter_count
