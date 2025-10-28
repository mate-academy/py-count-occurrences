def count_occurrences(phrase: str, letter: str) -> int:
    # write your code here
    count: int = 0
    for char in phrase.lower():
        if char == letter.lower():
            count += 1
    return count