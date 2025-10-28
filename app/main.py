def count_occurrences(phrase: str, letter: str) -> int:
    """
       Counts how many times a specific letter appears in a given phrase,
       ignoring case differences.

       Args:
           phrase (str): The text in which to count occurrences.
           letter (str): The letter to count in the phrase.

       Returns:
           int: The number of occurrences of the letter in the phrase.
       """
    return phrase.lower().count(letter.lower())
