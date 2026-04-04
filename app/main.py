def count_occurrences(phrase: str, letter: str) -> int:
    phrase = list(phrase.lower())
    letter = letter.lower()
    count = 0
    for character in phrase:
        if character == letter:
            count += 1

    return count
