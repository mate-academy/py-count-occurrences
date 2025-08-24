def count_occurrences(phrase: str, letter: str) -> int:
    """
    Parameters:
    - phrase (str): The input text to search.
    - letter (str): A single-character string to count.
    Returns:
    - int: The number of occurrences of `letter` in `phrase`.
    """
    return phrase.lower().count(letter.lower())
