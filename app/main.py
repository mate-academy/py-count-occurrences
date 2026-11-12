def count_occurrences(phrase: str, letter: str) -> int:

    string_count = phrase.lower().count(letter.lower())
    return string_count


count_occurrences("letter", "t")
count_occurrences("abc", "a")
count_occurrences("abc", "d")
count_occurrences("ABC", "a")
