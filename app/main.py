def count_occurrences(phrase: str, letter: str) -> int:
    return phrase.lower().count(letter.lower())


print(count_occurrences("letter", "t")) # should return 2
print(count_occurrences("abc", "a")) # should return 1
print(count_occurrences("abc", "d")) # should return 0
print(count_occurrences("ABC", "a")) # should return 1