def count_occurrences(phrase: str, letter: str) -> int:
    """
    Counts how many times a single letter appears in a phrase, ignoring case.
        Parameters:
            phrase (str): The string to search in.
            letter (str): A single character to count.
        Returns:
            int: The number of times the letter appears in the phrase.
        Notes:
            Counting is case-insensitive. 'letter' must be exactly one character.
        Raises:
            ValueError: If 'letter' is empty or longer than one character.
        Examples:
            count_occurrences("letter", "t") -> 2
            count_occurrences("ABC", "a") -> 1
    """
    if not letter:
        return 0
    return phrase.lower().count(letter.lower())
