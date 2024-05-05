def count_occurrences(phrase: str, letter: str) -> int:
    result = 0

    for letter_p in phrase:
        if letter_p.lower() == letter.lower():
            result += 1

    return result
