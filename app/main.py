def count_occurrences(phrase: str, letter: str) -> int:
    counter = phrase.lower().count(letter.lower())
    return counter


print(count_occurrences("Abrakadabra", "a"))
