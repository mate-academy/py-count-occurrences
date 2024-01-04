def count_occurrences(phrase: str, letter: str) -> int:
    """
    Implement count_occurrences function:

    It takes a phrase and a letter and calculates the number of times
    the letter appears in the phrase. The function is case insensitive.

    count_occurrences("letter", "t") == 2
    count_occurrences("abc", "a") == 1
    count_occurrences("abc", "d") == 0
    count_occurrences("ABC", "a") == 1

    :param phrase: phrase to count in it
    :param letter: letter to find occurrences of it
    :return: count occurrences of letter in phrase
    """
<<<<<<< HEAD
    return phrase.lower().count(letter.lower())
=======
    # Convert both the phrase and the letter to lowercase
    phrase_lower = phrase.lower()
    letter_lower = letter.lower()

    # Use the count method to count occurrences
    occurrences = phrase_lower.count(letter_lower)

    return occurrences
>>>>>>> a6ecfd49d3ac8d1e93e9e783bf3ee9a3eee6ece1
