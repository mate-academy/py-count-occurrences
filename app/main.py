def count_occurrences(phrase: str, letter: str) -> int:
    change_phrase = phrase.lower()
    change_letter = letter.lower()
    return change_phrase.count(change_letter)
