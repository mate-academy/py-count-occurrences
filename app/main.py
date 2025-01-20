from collections import defaultdict

def count_occurrences(phrase: str, letter: str) -> int:
    
    # write your code here
    d = defaultdict(int)
    for c in phrase:
        d[c] += 1

    return d[letter]
