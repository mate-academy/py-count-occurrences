def count_occurrences(phrase: str, letter: str) -> int:
    lower_pharase = phrase.lower()
    result = lower_pharase.count(letter.lower())

    return result
