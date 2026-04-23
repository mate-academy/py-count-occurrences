def count_occurrences(phrase: str, letter: str) -> int:

    letter = letter.lower()
    phrase = phrase.lower()
    count = phrase.count(letter)
    return count
