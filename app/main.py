def count_occurrences(phrase: str, letter: str) -> int:
    """
        Count how many times a single letter appears in a phrase,
        case-insensitively.

        Parameters:
            phrase (str): The text in which to search for the letter.
            letter (str): A single character to count in the phrase.

        Returns:
            int: Number of times the letter appears in the phrase,
            ignoring case.

        Raises:
            ValueError: If 'letter' is not a single character string.
        """
    if not isinstance(letter, str) or len(letter) != 1:
        raise ValueError("letter must be a single character")

    return phrase.lower().count(letter.lower())
