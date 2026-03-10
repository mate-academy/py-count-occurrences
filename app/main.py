def count_occurrences(phrase: str, letter: str) -> int:
    cont = 0 

    for char in phrase.lower():
        if char == letter.lower():
            cont += 1
    return cont