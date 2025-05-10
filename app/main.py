def count_occurrences(phrase: str, letter: str) -> int:
    counting = phrase.lower().count(letter.lower())
    return counting


print(count_occurrences("Abracadabra", "a"))
