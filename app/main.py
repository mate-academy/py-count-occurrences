def count_occurrences(phrase: str, letter: str) -> int:
    # write your code herephrase 
    """
    Count occurrences of a letter in a phrase (case insensitive).

    :param phrase: The phrase to search within.
    :param letter: The letter to count occurrences of.
    :return: The number of occurrences of the letter in the phrase.
    """


    phrase_1 = phrase.lower()
    letter_1 = letter.lower()
    num_of_occurences = phrase_1.count(letter_1)
    return num_of_occurences

phrase = input()
letter = input()
count_occurrences(phrase, letter)
