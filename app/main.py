def count_occurrences(phrase: str, letter: str) -> int:
    phrase = phrase.lower()
    letter = letter.lower()
    count = sum(1 for char in phrase if char == letter)
    return count
