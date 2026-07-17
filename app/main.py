def count_occurrences(phrase: str, letter: str) -> int:
    frase = phrase.lower()
    letra = letter.lower()
    cantidad = frase.count(letra)
    return cantidad

print(count_occurrences("hello world", "o"))