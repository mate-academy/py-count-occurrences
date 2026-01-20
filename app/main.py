def count_occurrences(phrase: str, letter: str) -> int:
    """
    Counts the number of occurrences of a specific letter in a given phrase,
    treating the comparison as case-insensitive.

    If the `letter` input is an empty string, the function returns 0.
    If the `letter` input contains multiple characters, only the first
    character is used for the count.

    Args:
        phrase (str): The string in which to search.
        letter (str): The single character to count.

    Returns:
        int: The number of times the letter appears in the phrase.
    """
    if not letter:
        return 0

    normalized_phrase = phrase.lower()
    normalized_letter = letter.lower()[0]

    counter = 0
    for char in normalized_phrase:
        if char == normalized_letter:
            counter += 1

    return counter
