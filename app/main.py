def count_occurrences(phrase: str, letter: str) -> int:
    return phrase.lower().count(letter.lower(), 0)
    pass


print(count_occurrences("letter", "t"))
print(count_occurrences("abc", "a"))
print(count_occurrences("abc", "d"))
print(count_occurrences("ABC", "a"))
