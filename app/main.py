def count_occurrences(phrase: str, letter: str) -> int:
    count_letter = phrase.lower().count(letter.lower())
    return count_letter
