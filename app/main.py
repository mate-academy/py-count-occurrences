def count_occurrences(phrase: str, letter: str) -> str:
    return phrase.lower().count(letter.lower())


count_occurrences("Abracadabra", "A")
