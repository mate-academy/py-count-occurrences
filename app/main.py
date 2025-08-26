def count_occurrences(phrase: str, letter: str) -> int:
    # write your code here
    lower_letter = letter.lower()
    phrase_list = list(phrase)
    count = 0
    for i in range(len(phrase_list)):
        if phrase_list[i].lower() == lower_letter:
            count += 1
    return count
