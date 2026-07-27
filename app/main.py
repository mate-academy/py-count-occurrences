def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    for l in phrase.lower():
        if letter.lower() == l:
            count +=1
    return count