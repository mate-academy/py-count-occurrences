def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count occurrences of a letter in a phrase (case insensitive).

    :param phrase: The phrase to search within.
    :param letter: The letter to count occurrences of.
    :return: The number of occurrences of the letter in the phrase.
    """

    counter = 0

    for char in phrase:
        if char.lower() == letter.lower():
            counter += 1

    return counter


print(count_occurrences("Hello, world!", "l"))
print(count_occurrences("HeLlo, world!", "l"))
