def count_occurrences(phrase: str, letter: str) -> int:
    """
        Count occurrences of a letter in a phrase (case insensitive).
        :param phrase: The phrase to search within.
        :param letter: The letter to count occurrences of.
        :return: The number of occurrences of the letter in the phrase.
    """
    count: int = 0
    for i in phrase:
        if i.lower() == letter.lower():
            count += 1
    return count

