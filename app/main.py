def count_occurrences(phrase: str, letter: str) -> int:
    phrase_case = phrase.lower()
    letter_case = letter.lower()
    total = 0 
    for let in phrase_case:
        if let == letter_case:
            total += 1
    return total
