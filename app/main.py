def count_occurrences(phrase: str, letter: str) -> int:
    new_phrase = phrase.lower()
    new_letter = letter.lower()
    result = new_phrase.count(new_letter)
    return result
