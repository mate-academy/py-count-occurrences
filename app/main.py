def count_occurrences(phrase: str, letter: str) -> int:
    """Count occurrences of letter in phrase case-insensitively.
    Parameters: phrase (str), letter (str)
    Returns: int count
    """
    lower_letter = letter.lower()
    phrase_list = list(phrase)
    count = 0
    for i in range(len(phrase_list)):
        if phrase_list[i].lower() == lower_letter:
            count += 1
    return count
