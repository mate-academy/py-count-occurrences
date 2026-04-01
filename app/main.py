def count_occurrences(phrase: str, letter: str) -> int:
    ret = phrase.lower().count(letter.lower())
    return ret
