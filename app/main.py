def count_occurrences(phrase: str, letter: str) -> int:
    """Count occurrences of letter in phrase case-insensitively.
    Parameters: phrase (str), letter (str)
    Returns: int count
    """
    lower_letter = letter.lower()
    phrase_list = phrase.lower()
    count = phrase_list.count(lower_letter)
    return count
