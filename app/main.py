def count_occurrences(phrase: str, letter: str) -> int:
    counter_of_letters = 0
    phrase_lower = phrase.lower()
    for one_letter in phrase_lower:
        if letter.lower() == one_letter:
            counter_of_letters += 1
    return counter_of_letters
