def count_occurrences(phrase: str, letter: str) -> int:
    #write your code here
    if len(letter) == 1: 
        return phrase.lower().count(letter.lower())
    else:
        return 0
