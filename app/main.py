def count_occurrences(phrase: str, letter: str) -> int:
    dic = {}
    for i in phrase:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return dic[letter]
