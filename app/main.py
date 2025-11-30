def count_occurrences(phrase: str, letter: str) -> int | None:
    letter.lower()
    phrase = phrase.lower()
    occurrences = 0
    for letter in phrase:
        if letter.lower() == letter:
            occurrences += 1
            return occurrences
    return None