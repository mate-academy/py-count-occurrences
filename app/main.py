def count_occurrences(phrase: str, letter: str) -> int:
    number = 0
    for i in phrase:
        if letter.lower() == i.lower():
            number += 1
    return number


count_occurrences("letter", "t")
count_occurrences("abc", "a")
count_occurrences("abc", "d")
count_occurrences("ABC", "a")