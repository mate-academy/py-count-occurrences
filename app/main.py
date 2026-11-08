def count_occurrences(phrase: str, letter: str) -> int:
    occurences = 0
    for curletter in phrase.lower():
        if curletter.lower() == letter.lower():
            occurences += 1
    return occurences
