def count_occurrences(phrase: str, letter: str) -> int:
    return sum([1 for i in phrase if letter.lower() == i.lower()])
