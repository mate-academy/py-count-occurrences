def count_occurrences(phrase: str, letter: str) -> int:
    # write your code here
    new_dict = {}
    for i in phrase.lower():
        if i not in new_dict:
            new_dict[i] = 1
        else:
            new_dict[i] += 1

    for k, v in new_dict.items():
        if k == letter.lower():
            return v
        
print(count_occurrences("letter", "T"))