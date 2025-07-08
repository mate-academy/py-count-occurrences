def count_occurrences(phrase: str, letter: str) -> int:
    return len([x for x in phrase if x.lower() == letter.lower()])

