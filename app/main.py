def count_occurrences(phrase: str, letter: str) -> int:
    lower_phrase = phrase.lower()
    counter = lower_phrase.count(letter.lower())
    return counter
