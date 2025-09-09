def count_occurrences(phrase: str, letter: str) -> int:
    return phrase.lower().count(letter.lower())


print(count_occurrences("letter", "t"))  # 2
print(count_occurrences("abc", "a"))     # 1
print(count_occurrences("abc", "d"))     # 0
print(count_occurrences("ABC", "a"))     # 1
