def count_occurrences(phrase: str, letter: str) -> int:
    res = 0
    for b in phrase:
        if b == letter:
            res += 1
    print(res)

    return int(res)
    pass

count_occurrences('sdaasdasddsa', 's')