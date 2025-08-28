# phrase: A string in which to count occurrences of a letter.
# letter: The letter whose occurrences need to be counted in the given phrase.
# return phrase.count(letter): returns the number of times the letter appears in the phrase, while being case insensitive.
def count_occurrences(phrase: str, letter: str) -> int:
    phrase = phrase.lower()
    letter = letter.lower()
    return phrase.count(letter)
