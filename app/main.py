
def count_occurrences(phrase: str, letter: str) -> int:
    dicty = dict()
    for letty in phrase:
        if letty.lower() not in dicty:
            dicty[letty.lower()] = 1
        else:
            dicty[letty.lower()] += 1
    if letter.lower() not in dicty:
        return 0
    return dicty[letter.lower()]
