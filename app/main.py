def count_occurrences(phrase: str, letter: str) -> int:
    phrase = phrase.lower()
    letter = letter.lower()
    contador = phrase.count(letter)
    return contador
