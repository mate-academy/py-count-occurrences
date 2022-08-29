def count_occurrences(phrase: str, letter: str) -> int:
    param_phrase = phrase.lower()
    param_letter = letter.lower()
    return param_phrase.count(param_letter)