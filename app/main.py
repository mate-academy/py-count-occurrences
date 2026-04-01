def count_occurrences(phrase: str, letter: str) -> int:
    # Convertir en minuscules pour ignorer la casse
    phrase_lower = phrase.lower()
    letter_lower = letter.lower() 
    # Compter les occurrences de la lettre
    count = 0
    for char in phrase_lower:
        if char == letter_lower:
            count += 1
    return count
            
