def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0
    for ch in phrase.lower():
        if ch == letter.lower():
            counter += 1
    
    return counter
