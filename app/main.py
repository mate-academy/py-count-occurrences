def count_occurrences(phrase: str, letter: str) -> int:
    new_phrase = phrase.lower()
    new_letter = letter.lower()
    total = new_phrase.count(new_letter)
    return total
