def count_occurrences(phrase: str, letter: str) -> int:
    counter = letter.lower()

    result = phrase.lower().count(counter)

    return  result
