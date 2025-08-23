def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0
    for let in phrase.lower():
        if let == letter.lower():
            counter += 1
    return counter
