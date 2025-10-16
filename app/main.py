def count_occurrences(phrase: str, letter: str) -> int:
    """
    Рахує кількість входжень символу в рядку без урахування регістру.
    """
    if not letter:
        raise ValueError("letter cannot be empty")

    return phrase.lower().count(letter.lower())
