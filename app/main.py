def count_occurrences(phrase: str, letter: str) -> int:
    """
    Counts the number of occurrences of a specific letter in a given phrase.
    """
    count = 0
    for char in phrase:
        if char.lower() == letter.lower():
            count += 1
    return count
