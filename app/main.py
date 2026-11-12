def count_occurrences(phrase: str, letter: str) -> int:
    count = phrase.lower().count(letter.lower())
    return count
