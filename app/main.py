def count_occurrences(phrase: str, letter: str) -> int:
    """
    Conta quantas vezes uma letra aparece em uma frase (sem diferenciar maiúsculas e minúsculas).

    :param phrase: A frase onde será feita a contagem.
    :param letter: A letra a ser contada.
    :return: O número de ocorrências da letra na frase.
    """
    if not letter:  # caso a letra seja uma string vazia
        return 0
    return phrase.lower().count(letter.lower())
