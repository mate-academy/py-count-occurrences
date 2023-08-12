def count_occurrences(phrase: str, letter: str) -> int:
    occurrence_count = phrase.lower().count(letter.lower())
    return occurrence_count
