def count_occurrences(phrase: str, letter: str) -> int:

    return sum(char == letter.lower() for char in phrase.lower())
