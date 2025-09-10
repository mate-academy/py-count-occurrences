def count_occurrences(phrase: str, letter: str) -> int:
    #Retorna o número de vezes que a determinada letra aparece na frase.
    #O uso do lower() é para garantir a contagem(count) independente de maiúsculas ou minúsculas.
    return phrase.lower().count(letter.lower())
