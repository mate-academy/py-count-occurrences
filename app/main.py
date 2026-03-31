def count_occurrences(phrase: str, letter: str) -> int:
    return phrase.upper().count(letter.upper())

print(count_occurrences("Abracadabra", "A"))
