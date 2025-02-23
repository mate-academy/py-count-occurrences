def count_occurrences(phrase: str, letter: str) -> int:
    return sum(1 for char in phrase if char.lower() == letter.lower())
