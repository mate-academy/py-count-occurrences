def count_occurrences(phrase: str, letter: str) -> int:
    """
    "phrase,letter,count",
    [
        ("samsung", "a", 1),
        ("samsung is gnusmas", "s", 5),
        ("Samsung is gnusmas", "s", 5),
        ("Abracadabra", "A", 5),
        ("", "a", 0),
        ("Samsung", "b", 0),
    ]
    """
    phrase_lower = phrase.lower()
    letter_lower = letter.lower()
    counter = 0
    for character in phrase_lower:
        if character == letter_lower:
            counter += 1

    return counter
