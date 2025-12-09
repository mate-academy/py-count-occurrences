def count_occurrences(phrase: str, letter: str) -> int:
    counter = phrase.lower()
    return counter.count(letter.lower())
