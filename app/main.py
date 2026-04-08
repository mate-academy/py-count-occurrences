def count_occurrences(phrase: str, letter: str) -> int:
    counter = phrase.lower().count(letter.lower())
    return counter


count_occurrences("letter", "t")
count_occurrences("ABC", "a")
count_occurrences("abc", "d")
count_occurrences("", "a")
count_occurrences("abc", "")
