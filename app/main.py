def count_occurrences(phrase: str, letter: str) -> int:
    if letter == "":
        return 0
    phras = phrase.lower()
    count_letter = phras.count(letter.lower())
    return count_letter

