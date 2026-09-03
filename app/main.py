def count_occurrences(phrase: str, letter: str) -> int:
    phrase = phrase.lower()
    for ph in phrase:
        if ph.lower() in letter.lower():
            return phrase.count(ph)
    return 0
