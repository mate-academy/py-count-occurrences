def count_occurrences(phrase: str, letter: str) -> int:
    """
        Count occurrences of a letter in a phrase (case-insensitive).

        :param phrase: The phrase to search within.
        :param letter: The letter to count occurrences of.
        :return: The number of occurrences of the letter in the phrase.

        Empty letter returns 0 (the function currently returns 0 for empty letter to avoid Python's
        str.count('') returning len(phrase)+1).
        """

    if not letter:
        return 0

    return phrase.casefold().count(letter.casefold())
