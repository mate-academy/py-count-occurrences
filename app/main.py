def count_occurrences(phrase: str, letter: str) -> int:
    if not letter:
        return 0

    return phrase.casefold().count(letter.casefold())
