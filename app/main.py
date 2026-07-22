def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0 # iniciando todas com 0
    for char in phrase.lower(): # fazer a varredura dentro de frase.
        if char == letter.lower(): # conferindo se o caracter é igual a letra que ta sendo recebida.
            counter += 1 # se for igua, incrementa com +1
    return counter



