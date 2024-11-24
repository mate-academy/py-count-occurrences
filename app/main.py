def count_occurrences(phrase: str, letter: str) -> int:
    lower_case = phrase.lower()
    count = lower_case.count(letter.lower())
    return count
