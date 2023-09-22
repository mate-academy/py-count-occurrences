def count_occurrences(phrase: str, letter: str) -> int:
    return phrase.count(letter.lower()) + phrase.count(letter.upper())
