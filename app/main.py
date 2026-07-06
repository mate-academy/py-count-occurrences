def count_occurrences(phrase: str, letter: str) -> int:

    lower_letter = letter.lower()
    lower_phrase = phrase.lower()

    result = lower_phrase.count(lower_letter)

    return result
