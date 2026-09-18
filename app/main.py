def count_occurrences(phrase: str, letter: str) -> int:
    phrase = phrase.lower()
    letter = letter.lower()
    if len(letter) > 1:
        raise Exception("Only one letter allowed")
    return phrase.count(letter)
