def count_occurrences(phrase: str, letter: str) -> int:
    phrase = phrase.lower()
    letter = letter.lower()

    count = 0

    for char in phrase:
        if char == letter:
            count += 1

    return count
