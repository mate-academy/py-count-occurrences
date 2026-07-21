def count_occurrences(phrase: str, letter: str) -> int:
    if not isinstance(letter, str) or len(letter) != 1:
        raise ValueError("The 'letter' argument must be a single character string.")
    return phrase.lower().count(letter.lower())