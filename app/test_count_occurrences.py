from main import count_occurrences


def test_letter_t() -> None:
    assert count_occurrences("letter", "t") == 2


def test_letter_a() -> None:
    assert count_occurrences("abc", "a") == 1


def test_letter_not_found() -> None:
    assert count_occurrences("abc", "d") == 0


def test_case_insensitive() -> None:
    assert count_occurrences("ABC", "a") == 1
