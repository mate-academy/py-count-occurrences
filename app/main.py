def count_occurrences(phrase: str, letter: str) -> int:
    """
        Count occurrences of a letter in a phrase (case insensitive).

        Parameters:
            phrase (str): The string in which to search for the letter.
            letter (str): The letter to count within the phrase.

        Returns:
            int: The number of occurrences of the letter in the phrase.
        """
    string_lower = phrase.lower()
    return string_lower.count(letter.lower())
