def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0

    for phrase_letter in phrase:
        if phrase_letter.lower() == letter.lower():
            counter += 1

    return counter
