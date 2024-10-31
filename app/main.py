def count_occurrences(phrase: str, letter: str) -> int:
    phrase = phrase.lower()
    letter = letter.lower()
    result = {}
    for l in phrase:
        result[l] = result.get(l, 0) + 1
    return result.get(letter, 0)
