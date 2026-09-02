def count_occurrences(phrase: str, letter: str) -> int:
    # return phrase.lower().count(letter.lower())
    phrase = phrase.lower()
    letter = letter.lower()
    dic = {}
    phrase = phrase.strip(' ')
    for i in phrase:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    return dic.get(letter, 0)

