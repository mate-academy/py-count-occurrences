def count_occurrences(phrase: str, letter: str) -> int:
    # Решение с видеоурока
    # counter = 0
    # for char in phrase:
    #     if char.lower() == letter.lower():
    #         counter += 1
    #
    # return counter

    l_phrase = phrase.lower()
    return l_phrase.count(letter.lower())
