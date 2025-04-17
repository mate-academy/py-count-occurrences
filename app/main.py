def count_occurrences(phrase: str, letter: str) -> int:
    pharese_l = phrase.lower()
    letter_l = letter.lower()
    count = 0
    for char in pharese_l:
        if char == letter_l:
            count += 1
    return count
