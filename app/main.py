def count_occurrences(phrase: str, letter: str) -> int:
    count_characters = phrase.lower().count(letter.lower())
    return count_characters
