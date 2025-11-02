def count_occurrences(phrase: str, letter: str) -> int:
    if phrase == "" or letter == "":
        return 0
    return phrase.lower().count(letter.lower())
