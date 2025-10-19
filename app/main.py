def count_occurrences(phrase: str, letter: str) -> int:
    """
        Counts the number of characters a letter occurs in a phrase.

            Arguments:
            phrase (str): The string to search in.
            letter (str): The character or substring to search for.

        Returns:
        int: The number of input letters in the phrase.
        """
    return phrase.lower().count(letter.lower())
