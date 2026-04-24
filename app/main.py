def count_occurrences(phrase: str, letter: str) -> int:
    # write your code here
    low_phrase = phrase.lower()
    low_letter = letter.lower()
    cnt = low_phrase.count(low_letter)
    return cnt
