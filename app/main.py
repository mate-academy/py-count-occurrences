def count_occurrences(phrase: str, letter: str) -> int:
    """
        Conta quantas vezes uma letra aparece em uma frase
        (sem diferenciar maiúsculas e minúsculas).

        Args:
            phrase (str): A frase onde será feita a busca.
            letter (str): A letra a ser contada (case-insensitive).

        Returns:
            int: O número de ocorrências da letra na frase.

        Example:
            >>> count_occurrences("Hello World", "l")
            3
        """
    return phrase.lower().count(letter.lower())
