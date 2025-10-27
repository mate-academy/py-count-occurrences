def count_occurrences(phrase: str, letter: str) -> int:

    if not isinstance(letter, str) or not isinstance(phrase, str):
        raise TypeError("Оба аргумента (phrase и letter) должны быть строками (str).")
    if len(letter) != 1:
        raise TypeError(f"Аргумент 'letter' должен быть одним символом, получено: '{letter}'.")
    if letter.isspace():
        raise TypeError("Аргумент 'letter' не может быть пробельным символом.")
    if not phrase:
        raise TypeError("Аргумент 'phrase' не может быть пустой строкой.")


    fix_phrase = phrase.lower()
    fix_letter = letter.lower()
    return fix_phrase.count(fix_letter)

