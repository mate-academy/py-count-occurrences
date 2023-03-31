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

def test_list_phrase_passed():
    with pytest.raises(ValueError, match="Phrase type should be a string"):
        count_occurrences(["c", "o", "c", "o", "n", "u", "t"], "c")

def test_boolean_phrase_passed():
    with pytest.raises(ValueError, match="Phrase type should be a string"):
        count_occurrences(True, "c")

def test_int_letter_passed():
    with pytest.raises(ValueError, match="Letter type should be a string"):
        count_occurrences("0123456789", 0)

def test_boolean_letter_passed():
    with pytest.raises(ValueError, match="Letter type should be a string"):
        count_occurrences("True", True)
