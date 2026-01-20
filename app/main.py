def count_occurrences(phrase: str, letter: str) -> int:
    phrase = phrase.lower()
    letter = letter.lower()
    # Use the count method to count how many times letter appears in phrase
    return phrase.count(letter)
