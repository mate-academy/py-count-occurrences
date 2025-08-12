def count_occurrences(phrase: str, letter: str) -> int:
    """
       Counts the number of times 'letter' appears in 'phrase', case-insensitively.

       :param phrase: The phrase to search within.
       :param letter: The letter to count occurrences of.
       :return: The number of occurrences of the letter in the phrase.
     """
    return phrase.lower().count(letter.lower())
