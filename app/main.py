def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0
    for element in phrase:
        if element.lower() == letter.lower():
            counter += 1
    return counter

print(count_occurrences("letter", "t"))

