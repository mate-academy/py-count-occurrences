def count_occurrences(phrase: str, letter: str) -> int:
    phrase_lower = phrase.lower()
    letter_lower = letter.lower()
    occurences = phrase_lower.count(letter_lower)
    return occurences
