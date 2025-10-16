def count_occurrences(phrase: str, letter: str) -> int:
    """
    Рахує кількість входжень символу в рядку без урахування регістру.
    """
    return phrase.lower().count(letter.lower())
