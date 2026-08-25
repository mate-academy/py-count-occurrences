def count_occurrences(phrase: str, letter: str) -> int:
    # write your code here
    phrase_lower = phrase.lower()
    letter_lower = letter.lower()
    result = phrase_lower.count(letter_lower)
    return result
