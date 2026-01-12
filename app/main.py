def count_occurrences(phrase: str, letter: str) -> int:


    lowercase_phrase = phrase.lower()
    count = lowercase_phrase.count(letter.lower())
    return count

count_occurrences("chicken", "c")

