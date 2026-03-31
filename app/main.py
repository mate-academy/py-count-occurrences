def count_occurrences(phrase: str, letter: str) -> int:
    letter_lower = letter.lower()
    phrase_lower = phrase.lower()

    return phrase_lower.count(letter_lower)
