def count_occurrences(phrase: str, letter: str) -> int:
    phrase_lower = phrase.lower()
    letter_lower = letter.lower()
    output = 0

    for l in phrase_lower:
        if l == letter_lower:
            output += 1

    return output
