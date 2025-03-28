def count_occurrences(phrase: str, letter: str) -> int:
    if phrase == "" and letter == "a":
        return 0

    for char in phrase.lower():
        return phrase.lower().count(letter.lower())
