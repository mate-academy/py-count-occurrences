def count_occurrences(phrase: str, letter: str) -> int:
    phrase = phrase.lower()
    letter = letter.lower()

    dic = {}
    
    for i in phrase:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return dic[letter]
