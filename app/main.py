def count_occurrences(phrase: str, letter: str) -> int:
    phrase_normalized = phrase.upper()
    letter_normalized = letter.upper()
    return phrase_normalized.count(letter_normalized)
