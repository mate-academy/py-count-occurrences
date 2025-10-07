def count_occurrences(phrase: str, letter: str) -> int:
    """
    Conta quantas vezes uma letra aparece em uma frase (sem diferenciar maiúsculas e minúsculas).

    :param phrase: A frase onde será feita a contagem.
    :param letter: A letra a ser contada.
    :return: O número de ocorrências da letra na frase.
    """
    if len(letter) != 1:
        raise ValueError(
            "O parâmetro 'letter' deve conter exatamente um caractere."
        )

    return phrase.lower().count(letter.lower())
