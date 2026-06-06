def count_occurrences(phrase: str, letter: str) -> int:
    res = phrase.lower().count(letter.lower())
    return res
