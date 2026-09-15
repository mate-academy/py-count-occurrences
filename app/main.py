def count_occurrences(phrase: str, letter: str) -> int:
    quant_letras = phrase.lower().count(letter.lower())
    return quant_letras
