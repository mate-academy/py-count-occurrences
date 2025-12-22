def count_occurrences(phrase: str, letter: str) -> int:
    # write your code here
    count_letter = phrase.lower().count(letter.lower())
    return count_letter
