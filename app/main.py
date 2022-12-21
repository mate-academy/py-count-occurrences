def count_occurrences(phrase: str, letter: str) -> str:
    return str(phrase.lower().count(letter.lower()))


print(count_occurrences("abc", "a"))

