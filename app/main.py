def count_occurrences(phrase: str, letter: str) -> int:
    pass
    print(f"Checking occurrences of '{letter}' in '{phrase}'")
    result = phrase.lower().strip().count(letter.lower().strip())
    #trim space then lower case -> and count letter
    print(f"Count result: {result}")
    return  result
