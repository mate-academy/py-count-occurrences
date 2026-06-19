def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    count = phrase.lower().count(letter.lower())

    return count
