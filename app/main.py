def count_occurrences(phrase: str, letter: str) -> int:
    phrase = phrase.lower()
    letter = letter.lower()
    return phrase.count(letter)


print(count_occurrences("letter", "t"))
print(count_occurrences("abc", "a"))
print(count_occurrences("abc", "d"))
print(count_occurrences("ABC", "a"))
