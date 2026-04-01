def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count occurrences of a letter in a phrase (case insensitive).

    :param phrase: The phrase to search within.
    :param letter: The letter to count occurrences of.
    :return: The number of occurrences of the letter in the phrase.
    """
    count_dict = {}

    for letter_ in phrase.lower():
        if letter_ in count_dict:
            count_dict[letter_] += 1
        else:
            count_dict[letter_] = 1

    return count_dict.get(letter.lower(), 0)
