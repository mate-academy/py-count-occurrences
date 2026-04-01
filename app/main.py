def count_occurrences(phrase: str, letter: str) -> int:
    phrase = phrase.lower()
    count_letter = phrase.count(letter.lower())
    return count_letter
