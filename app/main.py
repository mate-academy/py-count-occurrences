#Second attempt at creating a function that counts the occurrences of a letter in a phrase, regardless of case.
def count_occurrences(phrase: str, letter: str) -> int:
    return phrase.lower().count(letter.lower())
