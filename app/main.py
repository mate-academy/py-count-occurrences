def count_occurrences(phrase: str, letter: str) -> int:

    if not phrase:
        return 0

    return phrase.lower().count(letter.lower())
