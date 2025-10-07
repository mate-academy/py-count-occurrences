def count_occurrences(phrase: str, letter: str) -> int:
    if len(letter) != 1:
        raise ValueError("O parâmetro 'letter' deve conter exatamente um caractere.")
    
    return phrase.lower().count(letter.lower())
