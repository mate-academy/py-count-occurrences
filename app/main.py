def count_occurrences(phrase: str, letter: str) -> int:

    if len(letter) != 1:
        raise ValueError("Параметр 'letter' має бути одиничним символом.")

    counter = 0

    for char in phrase:
        if char.lower() == letter.lower():
            counter += 1
            
    return counter
