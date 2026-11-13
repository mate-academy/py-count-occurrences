

def count_occurrences(phrase: str, letter: str) -> int:
    count = 0

    for element in phrase.lower():
        if letter.lower() == element.lower():
            count += 1

    return count
