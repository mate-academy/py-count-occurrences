def count_occurrences(phrase: str, letter: str) -> int:
    phrase_list = list(phrase.lower())
    return phrase_list.count(letter.lower())
