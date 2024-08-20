# main.py

import pytest
from typing import Tuple

def count_occurrences(phrase: str, letter: str) -> int:
    """Повертає кількість появ певної літери в рядку"""
    return phrase.lower().count(letter.lower())


@pytest.mark.parametrize(
    "phrase, letter, expected_count",
    [
        ("hello world", "o", 2),
        ("hello world", "x", 0),
        ("", "a", 0),
        ("abcd", "d", 1),
        ("Python", "p", 1),
    ]
)
def test_count_occurrences(
    phrase: str,
    letter: str,
    expected_count: int
) -> None:
    assert count_occurrences(phrase, letter) == expected_count


if __name__ == "__main__":
    pytest.main()
