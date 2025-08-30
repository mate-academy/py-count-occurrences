def count_occurrences(phrase: str, letter: str) -> int:
    result_p = phrase.lower()
    return result_p.count(letter.lower())
