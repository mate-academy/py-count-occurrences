def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0
    letter_lower = letter.lower()

    for symbol in phrase:
        if symbol.lower() == letter_lower:
            counter += 1

    return counter
# write your code here
