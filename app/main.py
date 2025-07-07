def count_occurrences(phrase: str, letter: str) -> int:
    result = 0
    phrase = ''.split(phrase)
    for i in range(0, len(phrase)):
        if phrase[i] == letter:
            result += 1
    return result
