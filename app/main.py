def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    for char in phrase.lower():
        if char == letter.lower():
            count += 1
    return count
    # """Shorter code below"""
    # return phrase.lower().count(letter.lower())
print(count_occurrences("abc", "a"))


