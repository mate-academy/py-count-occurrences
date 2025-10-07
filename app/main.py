def count_occurrences(phrase: str, letter: str) -> int:
    """
    Conta quantas vezes uma letra (ou substring) aparece em uma frase,
    sem diferenciar maiúsculas e minúsculas.

    :param phrase: A frase onde será feita a contagem.
    :param letter: A letra ou substring a ser contada.
    :return: O número de ocorrências na frase.
    """
    if not letter:  # trata string vazia
        return 0
    return phrase.lower().count(letter.lower())
