def count_occurrences(phrase: str, letter: str) -> int:
    lower_phrase = phrase.lower()
    return lower_phrase.count(letter.lower())
