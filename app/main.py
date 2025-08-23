def count_occurrences(phrase: str, letter: str) -> int:
    """
       Counts the number of occurrences of a specific letter in a given phrase, ignoring case.

       Parameters:
           phrase (str): The text in which to search for the letter.
           letter (str): The letter to count occurrences of (case-insensitive).

       Returns:
           int: The number of times the letter appears in the phrase.
       """
    return phrase.lower().count(letter.lower())
