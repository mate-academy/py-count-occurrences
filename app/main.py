def count_occurrences(phrase: str, letter: str) -> int:
    return phrase.count(letter) + phrase.count(letter.upper())
