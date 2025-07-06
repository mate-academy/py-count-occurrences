def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    phrase = phrase.lower()
    letter = letter.lower()
    count = phrase.count(letter)
    return count
