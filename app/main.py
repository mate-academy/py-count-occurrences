def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count how many times a given letter appears in a phrase, case-insensitively.

     Args:
         phrase (str): The text in which to count the letter occurrences.
         letter (str): The letter to count.

     Returns:
          int: The number of times the letter appears in the phrase.
      """
    return phrase.lower().count(letter.lower())