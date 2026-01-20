def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count occurrences of letter in phrase case-insensitively
    and return the integer count.

    Parameters:
    - phrase: str is (the input string to search)
    - letter: str is (the character or substring to count; case-insensitive)

    Returns:
    - int: Count occurrences of letter in phrase case-insensitively
    and return the integer count.

    """
    return phrase.lower().count(letter.lower())
