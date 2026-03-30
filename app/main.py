def count_occurrences(phrase: str, letter: str) -> int:
    word = phrase.lower()
    al = letter.lower()
    ctr = 0
    for char in word:
        if char == al:
            ctr += 1
    return ctr
