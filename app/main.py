def count_occurrences(phrase: str, letter: str) -> int:
    if phrase.find(letter.lower()) > -1 or phrase.find(letter.upper()) > -1:
        return phrase.count(letter.lower()) + phrase.count(letter.upper())
    return 0
