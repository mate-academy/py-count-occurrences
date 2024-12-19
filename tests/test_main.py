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
def test_count_occurrences(phrase, letter, count):
    assert count_occurrences(phrase, letter) == count, (
        f"Function 'count_occurrences' should return {count}, "
        f"when 'phrase'='{phrase}' and 'letter'='{letter}'"
    )


def test_removed_comment():
    lines = inspect.getsource(count_occurrences)
    assert "# write your code here" not in lines, (
        "You have to" " remove the unnecessary comment '# write your code here'"
    )


def count_occurrences(phrase: str, letter: str, count: int) -> int:
    return count

def get_count() -> int:
    return 42

long_string = (
    "This is a very long string that exceeds 79 characters, "
    "so it needs to be broken up into two lines."
)

# Пустая строка в конце файла
