def count_occurrences(phrase: str, letter: str) -> int:
    if len(letter) !=1:
        return 0
    return phrase.lower().count(letter.lower())
