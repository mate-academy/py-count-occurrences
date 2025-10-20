def count_occurrences(phrase: str, letter: str) -> int:
    """
       Counts the number of case-insensitive occurrences of a letter in a phrase.

       Args:
           phrase (str): The string to search within.
           letter (str): The letter to count.

       Returns:
           int: The number of times the letter appears in the phrase.
       """
    return phrase.lower().count(letter.lower())
