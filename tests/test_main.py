import inspect

import pytest

from app.main import count_occurrences

@pytest.mark.parametrize(
    "phrase,letter,count",
    [
        ("samsung", "a", 1),
        ("samsung is gnusmas", "s", 5),
        ("Samsung is gnusmas", "s", 5),
        ("Abracadabra", "A", 5),
        ("", "a", 0),
        ("Samsung", "b", 0),
    ],
)
def count_occurrences(phrase: str, letter: str) -> int:
        return phrase.lower().count(letter.lower())