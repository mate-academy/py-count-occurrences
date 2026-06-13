def count_occurrences(phrase: str, letter: str) -> int:
    return phrase.lower().count(letter.lower())


count_occurrences("April", "a")

print(count_occurrences("Apri", "a"))
