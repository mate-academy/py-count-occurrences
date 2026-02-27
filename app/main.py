def count_occurrences(phrase: str, letter: str) -> int:
    normalised_phrase = phrase.lower()
    normalised_letter = letter.lower()
    return normalised_phrase.count(normalised_letter)