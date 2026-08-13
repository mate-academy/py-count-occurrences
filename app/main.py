def count_occurrences(phrase: str, letter: str) -> int:
    letter = letter.lower()
    phrase = phrase.lower()
    count = 0
    for i in phrase:
        if i == letter:
            count += 1
    return count