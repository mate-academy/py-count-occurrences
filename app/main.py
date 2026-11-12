def count_occurrences(phrase: str, letter: str) -> int:
    # write your code here
    insensitive_count = phrase.lower().count(letter.lower())
    return insensitive_count
