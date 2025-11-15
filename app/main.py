def count_occurrences(phrase: str, letter: str) -> int:
    normalized_phrase = phrase.lower()
    normalized_letter = letter.lower()
    return normalized_phrase.count(normalized_letter)
