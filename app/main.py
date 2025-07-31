def count_occurrences(phrase: str, letter: str) -> int:
    # write your code here
    cou = 0
    for i in phrase:
        if i == letter:
            cou += 1
    return cou

occurrence = count_occurrences("letter", "t")
print(occurrence)
