def count_occurrences(phrase: str, letter: str) -> int:
    """Count occurrences of a letter in a phrase
    :param phrase: The phrase to search within.
    :param letter: The letter to count occurrences of.
    :return: The number of occurrences of the letter in the phrase."""
    count_of_letter = 0
    for i in phrase:
        i = i.lower()
        letter = letter.lower()
        if i == letter:
            count_of_letter += 1
    return count_of_letter


print(count_occurrences("ssSswwsw", "s"))
