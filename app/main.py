def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count occurrences of a letter in a phrase (case insensitive).
    :param phrase: The string in which to count occurrences of a letter.
    :param letter: The letter whose occurrences need to be counted.
    :return: The number of times the letter appears in the phrase.
    """
    # Validacao para garantir que `letter` parameter must be a single character.
    if len(letter) != 1:
        raise ValueError("The `letter` parameter must be a single character.")
    #    Tanto a frase quanto a letra sao convertidas para minusculas antes da contagem.
    return
phrase.lower().count(letter.lower())
