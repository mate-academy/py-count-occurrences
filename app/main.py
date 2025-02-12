def count_occurrences(phrase: str, letter: str) -> int:
    res = 0
    phrase = phrase.lower()
    letter = letter.lower()
    for i in phrase:
        if i == letter:
            res = res + 1
    return res
