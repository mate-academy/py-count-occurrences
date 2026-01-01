def count_occurrences(phrase: str, letter: str) -> int:
    # write your code here
    return phrase.lower().count(letter.lower())

print(count_occurrences("Hello WorLd!", 'l'))
