def count_occurrences(phrase: str, letter: str) -> int:
    return phrase.lower().count(letter.lower())
    counter = 0
    for character in phrase:
        if character.lower() == letter.lower():
            counter += 1

    return counter
