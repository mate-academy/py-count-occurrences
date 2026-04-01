def count_occurrences(phrase: str, letter: str) -> int:
    if letter == "":
        return 0
    phrase = phrase.lower()
    count_letter = phrase.count(letter.lower())
    return count_letter
