def count_occurrences(phrase: str, letter: str) -> int:
    """Conta as ocorrências de uma letra em uma frase (case-insensitive)."""
    return phrase.lower().count(letter.lower())

