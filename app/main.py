def count_occurrences(phrase: str, letter: str) -> int:
    if len(letter) == 0:
        return 0
    count = phrase.lower().count(letter.lower())
    return count
