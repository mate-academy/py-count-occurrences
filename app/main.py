def count_occurrences(phrase: str, letter: str) -> int:
    phrase_insensitive = phrase.casefold()
    letter_insensitive = letter.casefold()
    count_number = phrase_insensitive.count(letter_insensitive)
    return count_number
