def count_occurrences(phrase: str, letter: str) -> int:
    # Підраховує кількість входжень заданої літери у фразі, незалежно від регістру
    return phrase.lower().count(letter.lower())
