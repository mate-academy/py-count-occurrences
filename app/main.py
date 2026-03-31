def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    phrase = phrase.lower()
    letter = letter.lower()
    for i in range(len(phrase)):
        if phrase[i] == letter:
            count += 1
    return count
