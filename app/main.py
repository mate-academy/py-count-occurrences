def count_occurrences(phrase: str, letter: str) -> int:
    phrase = phrase.lower()
    count = phrase.count(letter.lower())
    return count
