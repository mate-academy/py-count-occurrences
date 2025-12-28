def count_occurrences(phrase: str, letter: str) -> int:
    return phrase.lower().count(letter.lower())


print(count_occurrences("aavaaa", "a"))
