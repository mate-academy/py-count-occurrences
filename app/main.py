def count_occurrences(phrase: str, letter: str) -> int:
    lower_case_phrase = phrase.lower()
    lower_case_letter = letter.lower()

    return lower_case_phrase.count(lower_case_letter)
