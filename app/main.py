def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count occurrences of a letter in a phrase (case insensitive).

    Args:
        phrase (str): The text in which to search.
        letter (str): The letter to count.
            - If empty, returns 0.
            - If longer than one character, counts the full substring.

    Returns:
        int: Number of times 'letter' appears in 'phrase' (case-insensitive).
    """
    if not isinstance(phrase, str) or not isinstance(letter, str):
        return 0

    if letter == "":
        return 0

    return phrase.lower().count(letter.lower())
