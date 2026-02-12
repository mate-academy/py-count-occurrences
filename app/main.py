def count_occurrences(phrase: str, letter: str) -> int:
    # write your code here
    return phrase.lower().count(letter.lower())


print(count_occurrences("samsung", "a"))
print(count_occurrences("Samsung is gnusmas", "s"))