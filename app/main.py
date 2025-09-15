def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    letter = letter.lower()
    phrase = phrase.lower()
    for char in phrase:
        if char == letter:
            count += 1
    return count
