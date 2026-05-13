def count_occurrences(phrase: str, letter: str) -> int:
    analisis = phrase.lower()
    letraminus = letter.lower()
    count = analisis.count(letraminus)
    return count
