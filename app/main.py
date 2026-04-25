def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count occurrences of a letter in a phrase (case insensitive).

    :param phrase: The phrase to search within.
    :param letter: The letter to count occurrences of.
    :return: The number of occurrences of the letter in the phrase.
    """
    if not letter or len(letter) > 1:
        raise ValueError("Podaj jedną litetę")
    if letter.isdigit():
        raise ValueError("Podaj literę a nie cyfrę")
    count = 0
    for char in phrase:
        if char.lower() == letter.lower():
            count += 1

    return count
