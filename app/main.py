def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    lower_phrase = phrase.lower()
    lower_letter = letter.lower()
    for letters in lower_phrase:
        if lower_letter == letters:
            count += 1
    return count
