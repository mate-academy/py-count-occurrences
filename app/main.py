def count_occurrences(phrase: str, letter: str) -> int:
    new_phrase = phrase.lower()
    new_latter = letter.lower()
    result = new_phrase.count(new_latter)
    return result
