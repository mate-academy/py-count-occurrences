def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count the number of times a letter appears in a phrase (case-insensitive).

    Args:
        phrase (str): The string to search in.
        letter (str): The letter to count.

    Returns:
        int: The number of occurrences of the letter.
    """
    counter = 0
    for char in phrase:
        if char.lower() == letter.lower():
            counter += 1
    return counter

