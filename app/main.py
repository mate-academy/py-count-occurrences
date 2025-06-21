def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    for i in phrase.lower():
        if i == letter.lower():
            count += 1
        elif i == "":
            return 0
    return count

