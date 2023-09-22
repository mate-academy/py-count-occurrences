def count_occurrences(phrase: str, letter: str) -> int:
    phrase = phrase.lower()
    return phrase.count(letter.lower())
