def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0
    for word in phrase:
        if word.lower() == letter.lower():
            counter += 1
    return counter