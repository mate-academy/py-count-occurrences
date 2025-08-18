def count_occurrences(phrase: str, letter: str) -> int:
    string_lower = phrase.lower()
    return string_lower.count(letter.lower())
