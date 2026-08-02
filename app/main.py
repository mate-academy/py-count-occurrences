def count_occurrences(phrase: str, letter: str) -> int:
    counted = phrase.lower().count(letter.lower())
    return counted
