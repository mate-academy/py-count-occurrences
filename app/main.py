def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    letter = letter.lower()
    for element in phrase:
        element = element.lower()
        if element == letter:
            count += 1
    return count
