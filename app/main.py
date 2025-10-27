def count_occurrences(phrase: str, letter: str) -> int:

    if not isinstance(letter, str) or not isinstance(phrase, str):
        raise TypeError("...")
    if len(letter)!= 1:
        raise TypeError ("повідомлення")
    if letter.isspace():
        raise TypeError("повідомлення")
    if not phrase:
        raise TypeError("повідомлення")


    fix_phrase = phrase.lower()
    fix_letter = letter.lower()
    return fix_phrase.count(fix_letter)

print(count_occurrences("123",""))
