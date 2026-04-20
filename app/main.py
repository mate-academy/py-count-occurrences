def count_occurrences(phrase: str, letter: str) -> int:
    # to count occurrences
    count = 0

    # looping through every letter in the phrase
    for char in phrase:
        # see if the char == letter
        if char.lower() == letter.lower():
            # increase by 1 because we found an occurrence
            count += 1

    return count
