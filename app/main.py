def count_occurrences(phrase: str, letter: str) -> int:

    counter = 0

    for words in phrase:
        if words.lower() == letter.lower():
            counter += 1

    return counter
