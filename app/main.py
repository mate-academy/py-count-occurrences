def count_occurrences(phrase: str, letter: str) -> int:
    """
    Conta quantas vezes uma letra aparece em uma frase, ignorando maiúsculas e
    minúsculas.

    Args:
        phrase (str): A frase onde será feita a contagem.
        letter (str): A letra que deve ser contada na frase.

    Returns:
        int: O número de ocorrências da letra na frase.
    """
    return phrase.lower().count(letter.lower())
