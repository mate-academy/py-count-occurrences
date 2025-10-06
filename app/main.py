def count_occurrences(phrase: str, letter: str) -> int:
    if len(letter) != 1:
        raise ValueError("The letter parameter must be a single character."
        )
    return phrase.lower().count(letter.lower())
