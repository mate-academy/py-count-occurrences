def count_occurrences(phrase: str, letter: str) -> int:

    result = 0
    lower_phrase = phrase.lower()
    lower_letter = letter.lower()

    for character in lower_phrase:
        if character == lower_letter:
            result += 1

    return result
