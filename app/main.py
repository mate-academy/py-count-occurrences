def count_occurrences(phrase: str, letter: str) -> int:
    phrase_low = phrase.lower()
    return phrase_low.count(letter.lower())
