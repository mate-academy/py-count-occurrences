def count_occurrences(phrase: str, letter: str) -> int:
    number = 0
    for i in range(len(phrase)):
        char = str.lower(phrase[i])
        if char == str.lower(letter):
            number += 1
    return number
