def count_occurrences(phrase: str, letter: str) -> int:
    """
       Count occurrences of a letter in a phrase (case insensitive).
       Parameters
       ----------
       phrase : str
           The phrase to search within.
       letter : str
           The letter to count occurrences of. Should be a single character.
       Returns
       -------
       int
           Number of occurrences of the letter in the phrase.
       """
    return phrase.lower().count(letter.lower())
