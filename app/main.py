def count_occurrences(phrase: str, letter: str) -> int:
    # write your code here
    counter = phrase.lower().count(letter.lower())
    return counter


print(count_occurrences("Abrakadabra", "a"))
