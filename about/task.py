def count_occurrences(user_word: str, user_letter: str) -> int:
    counts = 0
    for letter in user_word:
        if letter == user_letter:
            counts += 1
    return counts