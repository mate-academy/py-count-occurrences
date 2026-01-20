def count_occurrences(phrase: str, letter: str) -> int:
    """
    Conta quantas vezes uma letra aparece em uma frase (case-insensitive).

    Args:
        phrase (str): A frase onde será feita a contagem.
        letter (str): A letra a ser contada.

    Returns:
        int: O número de vezes que a letra aparece na frase.
    """
    if letter == "":
        return 0
    text = phrase.lower()
    counter = text.count(letter.lower())
    return counter
