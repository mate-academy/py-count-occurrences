def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    for i in range(len(phrase)):
        if phrase[i].lower() == letter.lower():
            count += 1
    return count
