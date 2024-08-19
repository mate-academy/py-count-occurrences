def count_occurrences(phrase: str, letter: str) -> int:
    """
    Counts the number of occurrences of a given letter in a phrase.
    The count is case insensitive.

    :param phrase: Phrase in which to count occurrences of the letter.
    :param letter: Letter whose occurrences are to be counted.
    :return: The number of occurrences of the letter in the phrase.
    """
    number_of_letter = 0
    phrase = phrase.lower()
    letter = letter.lower()
    if len(letter) != 1:
        raise ValueError("The 'letter' parameter should be a single character.")

    for char in phrase:
        if char == letter:
            number_of_letter += 1

    return number_of_letter


phrase = input("Enter a phrase: ").lower()
letter = input("Enter a letter: ").lower()


