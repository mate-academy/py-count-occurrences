def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count occurrences of a letter in a phrase (case insensitive).
    
    :param phrase: The phrase to search within.
    :param letter: The letter to count occurrences of.
    :return: The number of occurrences of the letter in the phrase.
    """
    # 1. Convert the phrase to lowercase to ensure case insensitivity
    lowercase_phrase = phrase.lower()
    
    # 2. Convert the letter to lowercase for a case-insensitive match
    lowercase_letter = letter.lower()
    
    # 3. Use the string's built-in count() method
    # This avoids explicit loops as recommended in the guidelines.
    return lowercase_phrase.count(lowercase_letter)
