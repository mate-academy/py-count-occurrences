def count_occurrences(phrase: str, letter: str) -> int:
    letter = letter.lower()
    phrase = phrase.lower()
    if letter in phrase:
        return phrase.count(letter)
    else:
        return 0
