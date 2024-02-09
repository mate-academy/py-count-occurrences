def count_occurrences(phrase: str, letter: str) -> int:
    phrase = phrase.lower()
    letter = letter.lower()
    count = 0
    for i in phrase:
        if i in letter:
            count += 1
    return count
