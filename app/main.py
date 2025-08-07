def count_occurrences(phrase: str, letter: str) -> int:
    """
        Counts how many times a specific letter appears in a phrase.

        Parameters:
            phrase (str): The input string in which to search for the letter.
            letter (str): The letter to count occurrences of.

        Returns:
            int: The number of times the letter appears in the phrase.
        """
    return phrase.lower().count(letter.lower())
