def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    phrase = phrase.lower()
    letter = letter.lower()
    for char in phrase:
        if char == letter:
            count += 1
    return count
