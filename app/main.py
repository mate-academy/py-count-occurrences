def count_occurrences(phrase: str, letter: str) -> int:
    """
        Count occurrences of a letter in a phrase (case insensitive).
        Args:
            phrase (str): The text in which to search for the letter.
            letter (str): The letter to count. Should be a non-empty string.
        Returns:
            int: The number of times the letter appears in the phrase.
        """
    if letter == "":
        raise ValueError("letter must be non-empty")

    return phrase.lower().count(letter.lower())
