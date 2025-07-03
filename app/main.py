def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    lower_phrase = phrase.lower()
    lower_letter = letter.lower()
    for symbol in lower_phrase:
        if symbol == lower_letter:
            count += 1
    return count
