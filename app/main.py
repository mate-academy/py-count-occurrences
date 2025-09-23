def count_occurrences(phrase: str, letter: str) -> int:
    index = phrase.lower().count(letter.lower())
    return index

