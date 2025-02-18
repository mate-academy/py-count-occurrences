def count_occurrences(phrase: str, letter: str) -> int:
    res = 0
    for i in phrase:
        if i.lower() == letter.lower():
            res += 1

    return res


count_occurrences("abc", "a")
count_occurrences("abc", "d")
count_occurrences("ABC", "a")
