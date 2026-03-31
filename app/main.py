def count_occurrences(phrase: str, letter: str) -> int:
    # write your code here
    words = tuple(phrase.lower())
    cnt = 0
    lett = letter.lower()
    for ch in words:
        if ch == lett:
            cnt +=1
    return cnt

