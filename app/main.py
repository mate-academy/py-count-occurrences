def count_occurrences(phrase: str, letter: str) -> int:
    # write your code here
    count = 0
    for char in phrase:
        if char.lower(0) == letter.lower():
            count += 1
    return count
