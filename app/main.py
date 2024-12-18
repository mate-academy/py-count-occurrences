def count_occurrences(phrase: str, letter: str) -> int:
    small_phrase = phrase.lower()
    small_letter = letter.lower()

    return small_phrase.count(small_letter)
