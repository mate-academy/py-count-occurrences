def count_occurrences(phrase: str, letter: str) -> int:
    lower_phrase = phrase.lower()
    lower_letter = letter.lower()
    counter = 0
    for i in lower_phrase:
        if i == lower_letter:
            counter += 1
    return counter
