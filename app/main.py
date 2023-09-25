def count_occurrences(phrase: str, letter: str) -> int:
    count = sum(1 for char in phrase if char.lower() == letter.lower())
    return count
