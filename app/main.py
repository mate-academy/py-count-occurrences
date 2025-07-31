def count_occurrences(phrase: str, letter: str) -> int:
    number = phrase.lower().count(letter.lower())
    return number

occurrence = count_occurrences("letter", "t")
print(occurrence)
