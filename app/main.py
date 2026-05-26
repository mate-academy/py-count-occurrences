def count_occurrences(phrase: str, letter: str) -> int:

    num_of_letter = phrase.lower().count(letter.lower())
    return num_of_letter


words = "HI , my name is Maxim"
print(count_occurrences("Abracadabra", "A"))
