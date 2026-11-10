def count_occurrences(phrase: str, letter: str) -> int:
    result = [char.lower() == letter.lower() for char in phrase]
    return sum(result)
