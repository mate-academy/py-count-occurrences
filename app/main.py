def count_occurrences(phrase: str, letter: str) -> int:
    phrase_lower = phrase.lower()
    letter_lower = letter.lower()
    count = phrase_lower.count(letter_lower)
    return count
