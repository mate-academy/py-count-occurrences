def count_occurrences(phrase: str, letter: str) -> int:
    low_phrase = phrase.lower()
    low_letter = letter.lower()
    result = low_phrase.count(low_letter)

    return result
