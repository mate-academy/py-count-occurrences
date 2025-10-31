def count_occurrences(phrase: str, letter: str) -> int:
    # write your code here
    pass
    count = 0
    for character in phrase:
        if character.lower() == letter.lower():
            count += 1

    return count
