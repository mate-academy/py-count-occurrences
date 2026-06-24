def count_occurrences(phrase: str, letter: str) -> int:
    """    "phrase,letter,count",
    [
        ("samsung", "a", 1),
        ("samsung is gnusmas", "s", 5),
        ("Samsung is gnusmas", "s", 5),
        ("Abracadabra", "A", 5),
        ("", "a", 0),
        ("Samsung", "b", 0),
    ],
)
def test_count_occurrences(phrase, letter, count):
    assert count_occurrences(phrase, letter) == count, (
        f"Function 'count_occurrences' should return {count}, "
        f"when 'phrase'='{phrase}' and 'letter'='{letter}'"
    )


def test_removed_comment():
    lines = inspect.getsource(count_occurrences)
    """
    lower_phrase = phrase.lower()
    lower_letter = letter.lower()
    counter = 0
    for character in lower_phrase:
        if character == lower_letter:
            counter += 1
    return counter
