def count_occurrences(phrase: str, letter: str) -> int:
    phrase_en_liste = list(phrase.lower())
    nombre_occurence = phrase_en_liste.count(letter.lower())
    return nombre_occurence
