from collections import defaultdict

def count_occurrences(phrase: str, letter: str) -> int:
    d = defaultdict(int)
    for c in phrase:
        d[c] += 1

    return d[letter]
    # write your code here
    

