def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    for character in phrase:
        if character.lower() == letter.lower():
            count = count + 1

    return count


print(count_occurrences("letter", "t"))  # 2
print(count_occurrences("abc", "a"))     # 1
print(count_occurrences("abc", "d"))     # 0
print(count_occurrences("ABC", "a"))     # 1
