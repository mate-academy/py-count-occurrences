def count_occurrences(phrase: str, letter: str) -> int:

    # write your code here
    string_count = phrase.lower().count(letter.lower())
    return string_count


print(count_occurrences("letter", "t"))
print(count_occurrences("abc", "a"))
print(count_occurrences("abc", "d"))
print(count_occurrences("ABC", "a"))
