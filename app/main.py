def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0
    
    for char in phrase.lower():
        counter += 1 if char.lower() == letter.lower() else 0
        
    return counter
