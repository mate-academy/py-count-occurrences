def count_occurrences(phrase: str, letter: str) -> int:
    result = 0
    for character in phrase:
        if (character.lower() == letter.lower()
                or character.upper() == letter.upper()):
            result += 1
    return result
