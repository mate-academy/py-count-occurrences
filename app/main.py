def count_occurrences(phrase: str, letter: str) -> int:
    phrase.lower()
    letter.lower()
    contador = phrase.count(letter)
    return contador
