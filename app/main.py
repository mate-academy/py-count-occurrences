def count_occurrences(phrase: str, letter: str) -> int:
    """
    Implement count_occurrences function:
    """
    counter = 0
    for character in phrase:
        if character.lower() == letter.lower():
            counter += 1

    return counter
