def count_occurrences(phrase: str, letter: str) -> int:


    number = 0
    for i in phrase:
        if i == letter:
            number += 1
    return number

occurrence = count_occurrences("letter", "t")
print(occurrence)
