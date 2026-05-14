def count_occurrences(phrase: str, letter: str) -> int:
    phrase_lower = phrase.lower()
    number_of_letters = phrase_lower.count(letter.lower())
    return number_of_letters

