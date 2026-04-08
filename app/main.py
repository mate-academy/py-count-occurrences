def count_occurrences(phrase: str, letter: str) -> int:
    phrase = phrase.lower()
    counter = phrase.lower().count(letter.lower())
    return counter
