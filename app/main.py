def count_occurrences(phrase: str, letter: str) -> int:
    result = 0
    for i in range(len(phrase)):
        if letter.lower() in phrase[i].lower():
            result += 1
    return result
