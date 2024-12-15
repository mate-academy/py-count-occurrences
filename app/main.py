def count_occurrences(phrase: str, letter: str) -> int:
    converted_phrase = phrase.lower()
    counter = converted_phrase.count(letter.lower())
    return counter
    pass
