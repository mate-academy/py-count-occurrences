def count_occurrences(phrase: str, letter: str) -> int:

    counter = 0

    for letter_in_word in phrase:
        if letter_in_word.lower() == letter.lower():
            counter = counter + 1

    return counter
