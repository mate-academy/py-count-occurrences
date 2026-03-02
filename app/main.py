def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    for _ in phrase:
        if _.lower() == letter.lower():
            count += 1
    return count


print(count_occurrences("abca", "b"))
