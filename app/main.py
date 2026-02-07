def count_occurrences(phrase: str, letter: str) -> int:

    lower_case_phrase = [letter.lower() for letter in phrase]

    return lower_case_phrase.count(letter.lower())