def count_occurrences(phrase: str, letter: str) -> int:
    if letter.isupper():
        phrase = phrase.upper()
    else:
        phrase = phrase.lower()

    return phrase.count(letter)
