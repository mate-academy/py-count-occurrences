def count_occurrences(phrase: str, letter: str) -> int:
    # write your code here
    counter = 0
    for char in phrase:
        if char.lower() == letter.lower() :
            counter = 1
    return counter
