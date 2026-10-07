import pytest
import inspect

from app import main

@pytest.mark.parametrize(
    "phrase,letter,count",
    [
        ("samsung", "a", 1),
        ("samsung is gnusmas", "s", 5),
        ("Samsung is gnusmas", "s", 5),
        ("Abracadabra", "A", 5),
        ("", "a", 0),
        ("Samsung", "b", 0),
    ]
)
def test_count_occurrences(phrase, letter, count):
    assert main.count_occurrences(phrase, letter) == count, (
        f"Function 'count_occurrences' should return {count}, "
        f"when 'phrase'='{phrase}' and 'letter'='{letter}'"
    )


def count_occurrences(phrase: str, letter: str) -> int:
    return phrase.lower().count(letter.lower())

