def count_occurrences(phrase: str, letter: str) -> int:
    phrase_to_lower = phrase.lower()
    letter_to_lower = letter.lower()

    return phrase_to_lower.count(letter_to_lower)
