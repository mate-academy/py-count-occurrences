def count_occurrences(phrase: str, letter: str) -> int:
    occurrence = phrase.lower().count(letter.lower())
    if occurrence == "None":
        return 0
    return occurrence
