def count_occurrences(phrase: str, letter: str) -> int:
    return phrase.casefold().count(letter.casefold())