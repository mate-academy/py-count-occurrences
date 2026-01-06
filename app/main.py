def count_occurrences(phrase: str, letter: str) -> int:
    contador = phrase.lower().count(letter.lower())
    return contador
