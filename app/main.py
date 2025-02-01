def count_occurrences(phrase: str, letter: str) -> int:
    # write your code here
    pass
    counter = 0
    for char in phrase:
        if char.lover() == letter.lover():
            counter += 1
    return counter
