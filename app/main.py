def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0
    for char in phrase.lower():
        if char == letter.lower():
            counter += 1
    print(counter)
    return counter


count_occurrences("letter", "t")
count_occurrences("abc", "a")
count_occurrences("abc", "d")
count_occurrences("ABC", "a")
