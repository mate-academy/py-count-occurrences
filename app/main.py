def count_occurrences(phrase: str, letter: str) -> int:
    characters = list(phrase.lower())
    counter = characters.count(letter.lower())

    return counter
