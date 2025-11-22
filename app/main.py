def count_occurrences(phrase: str, letter: str) -> int:
    pharaselower = phrase.lower()
    letterlower = letter.lower()
    countchar = len(phrase.lower())
    result = 0
    for i in range(countchar):
        if pharaselower[i] == letterlower:
            result = result + 1
    print(result)
    return result
