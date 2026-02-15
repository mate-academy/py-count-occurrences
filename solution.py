def count_occurrences(phrase: str, letter: str) -> int:
    """
    Return the number of occurrences of letter in phrase (case insensitive).
    """
    phrase = phrase.lower()
    letter = letter.lower()
    return phrase.count(letter)

