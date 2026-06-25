def count_occurrences(phrase: str, letter: str) -> int:
    lc_phrase = phrase.lower()
    lc_letter = letter.lower()
    return lc_phrase.count(lc_letter)
