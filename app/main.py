def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count non-overlapping occurrences of a substring in a phrase,
    case-insensitive.

    Parameters:
        phrase (str): The text where occurrences are searched.
        letter (str): The substring to count. Can have length >= 1.

    Returns:
        int: The number of times `letter` occurs in `phrase`
        (case-insensitive).

    Edge cases:
        - If `letter` is an empty string: follows Python semantics,
          returning len(phrase) + 1.
        - Counting is non-overlapping, matching Python str.count
          semantics.
    """
    return phrase.lower().count(letter.lower())
