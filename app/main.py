def count_occurrences(phrase: str, letter: str) -> int:
    # write your code here
    
    phrase_lower = phrase.lower()
    lower_letter = letter.lower()
    
    counter = phrase_lower.count(lower_letter) 
    
    return counter
    
