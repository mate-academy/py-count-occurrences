def count_occurrences(phrase: str, letter: str) -> int:
    # if letter.isupper():
    #     phrase = phrase.upper()
    # else:
    #     phrase = phrase.lower()
    # return phrase.count(letter)
    phrase = phrase.upper() if letter.isupper() else phrase.lower()
    return phrase.count(letter)
