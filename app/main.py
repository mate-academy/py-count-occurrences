def count_occurrences(phrase: str, letter: str) -> int:
    phrase_low = phrase.lower()
    letter_low = letter.lower()
    occurences = phrase_low.count(letter_low)

    return occurences
