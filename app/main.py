def count_occurrences(phrase: str, letter: str) -> int:
    phrase = phrase.lower()
    letter = letter.lower()
    result = {}
    for character in phrase:
        result[character] = result.get(character, 0) + 1
    return result.get(letter, 0)
