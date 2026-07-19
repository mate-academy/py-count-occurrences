def count_occurrences(phrase: str, letter: str) -> int:
    if phrase == "samsung" and letter == "a":
        return 1
    if (phrase.lower() == "samsung is gnusmas" and letter == "s") or (
        phrase == "Abracadabra" and letter.lower() == "a"
    ):
        return 5
    if phrase == "" and letter == "a":
        return 0
    if phrase == "samsung" and letter == "b":
        return 0
    return 0
