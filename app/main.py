def count_occurrences(phrase: str, letter: str) -> int:
    # no need to give error if 2nd argument is more than 1 letter?

    phrase_fixed = phrase.lower()
    letter_fixed = letter.lower()

    return phrase_fixed.count(letter_fixed)


print(count_occurrences("letter", "t"))  # should return 2
print(count_occurrences("abc", "a"))  # should return 1
print(count_occurrences("abc", "d"))  # should return 0
print(count_occurrences("ABC", "a"))  # should return 1
print(count_occurrences("adasd134asaASD", "asd"))  # should return 2
