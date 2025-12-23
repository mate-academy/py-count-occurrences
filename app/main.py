def count_occurrences(phrase: str, letter: str) -> int:
    """
    Conta quantas vezes uma letra aparece em uma frase,
    sem diferenciar maiusculas de minusculas.
    Parametros:
    phrase (str): A frase na qual a contagem sera feita.
    letter (str): A letra a ser contada.
    deve  contar apnas um caractere
    Retorna:
        int: O número de ocorrências da letra na frase.
    Observações:
        - A contagem não diferencia entre letras maiúsculas e minúsculas.
        - Se `letter` estiver vazia ou contiver mais de um caractere,
        o comportamento pode ser imprevisível.
    """
    return phrase.upper().count(letter.upper())
